SELECT COUNT(a.id) AS fish_count
FROM FISH_INFO a
JOIN FISH_NAME_INFO b ON a.fish_type = b.fish_type
WHERE a.fish_type IN (
    SELECT fish_type FROM FISH_NAME_INFO WHERE fish_name = 'BASS'
)
OR a.fish_type IN (
    SELECT fish_type FROM FISH_NAME_INFO WHERE fish_name = 'SNAPPER'
);
