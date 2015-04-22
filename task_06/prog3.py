dat = pl.imread('data/MV_HFV_012.jpg')
dat = dat[60:]
filtdat = ndimage.median_filter(dat, size=(7,7))
hi_dat = np.histogram(dat, bins=np.arange(256))
hi_filtdat = np.histogram(filtdat, bins=np.arange(256))
void = filtdat <= 50
sand = np.logical_and(filtdat > 50, filtdat <= 114)
glass = filtdat > 114
phases = void.astype(np.int) + 2*glass.astype(np.int) 
3*sand.astype(np.int)
sand_op = ndimage.binary_opening(sand, iterations=2)
sand_labels, sand_nb = ndimage.label(sand_op)
sand_areas = np.array(ndimage.sum(sand_op, sand_labels, 
np.arange(sand_labels.max()+1)))
mask = sand_areas > 100
remove_small_sand 
mask[sand_labels.ravel()].reshape(sand_labels.shape)
bubbles_labels, bubbles_nb = ndimage.label(void)
bubbles_areas = np.bincount(bubbles_labels.ravel())[1:]
mean_bubble_size = bubbles_areas.mean()
median_bubble_size = np.median(bubbles_areas)
mean_bubble_size, median_bubble_size
(1699.875, 65.0)
