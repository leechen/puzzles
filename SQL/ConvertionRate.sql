SELECT
    device_type,
    instance,
    SUM(converted) AS conversions,
    COUNT(*) AS total_users,
    SUM(converted) * 1.0 / COUNT(*) AS conversion_rate
FROM
    experiment_data
WHERE
    experiment_name = 'New Experiment'
    AND device_type IN ('iPhone', 'iPad')
GROUP BY
    device_type,
    instance;
