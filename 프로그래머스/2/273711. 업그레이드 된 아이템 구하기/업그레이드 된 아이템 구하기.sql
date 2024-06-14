select b.item_id ,a.ITEM_NAME,a.RARITY from item_info as a
join item_tree as b on a.item_id = b.item_id
where b.parent_item_id in (
select item_id from item_info 
where rarity = "RARE")
order by a.item_id desc