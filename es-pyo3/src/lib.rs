use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use elasticsearch::{Elasticsearch, SearchParts};
use serde_json::json;

#[pymodule]
fn es_pyo3(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fetch_complex_query_py, m)?)?;
    Ok(())
}

#[pyfunction]
fn fetch_complex_query_py() -> PyResult<String> {
    let es = Elasticsearch::new(elasticsearch::http::transport::Transport::single_node("http://localhost:9200").unwrap());

    let query = json!({
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "number": {
                                "gte": 100,
                                "lte": 200
                            }
                        }
                    },
                    {
                        "match": {
                            "job": "engineer"
                        }
                    }
                ]
            }
        }
    });
    let rt = tokio::runtime::Builder::new_current_thread()
        .enable_time()
        .enable_io()
        .build()
        .unwrap();

    let response = rt.block_on(
        es.search(SearchParts::Index(&["sample_data"]))
            .body(query)
            .send()
    ).unwrap();

    let result: serde_json::Value = rt.block_on(response.json()).unwrap();

    Ok(result.to_string())

}
