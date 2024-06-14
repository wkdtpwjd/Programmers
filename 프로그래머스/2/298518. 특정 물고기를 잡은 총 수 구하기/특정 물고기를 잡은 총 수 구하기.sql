-- 코드를 작성해주세요
select count(a.id) as fish_count from FISH_INFO a
join FISH_NAME_INFO b on a.fish_type = b.fish_type
where b.fish_name in ('BASS','SNAPPER')