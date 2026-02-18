resource "google_storage_bucket" "taxi_bucket" {
  name     = "${var.project_id}-taxi-data"
  location = var.region
}

resource "google_bigquery_dataset" "taxi_dataset" {
  dataset_id = "ny_taxi"
  location   = var.region
}

resource "google_bigquery_table" "green_trips" {
  dataset_id = google_bigquery_dataset.taxi_dataset.dataset_id
  table_id   = "green_taxi_trips"
  deletion_protection = false
}
