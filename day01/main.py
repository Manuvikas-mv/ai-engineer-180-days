def calculate_success_rate(records):
    if not records:
        return 0.0

    successful = sum(
        1 for record in records
        if record["status"] == "success"
    )

    return round(successful / len(records) * 100, 2)


if __name__ == "__main__":
    pipeline_runs = [
        {"pipeline": "bronze", "status": "success"},
        {"pipeline": "silver", "status": "failed"},
        {"pipeline": "gold", "status": "success"}
    ]

    rate = calculate_success_rate(pipeline_runs)
    print(f"Pipeline success rate: {rate}%")