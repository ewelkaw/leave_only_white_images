1. **Running:**
```bash
python3 check_images.py images/ delete
```
python3 check_images.py path_to_images option_if_we_want_to_delete_non_slides


2. **CV2 installation:**

`pip install opencv-python`

From: `https://pypi.org/project/opencv-python/`

3. **Pixels threshold**

`pixels_thershold` is set to 50% (0.5) and it was set arbitrarily, so it can be changed anytime. If we want to check if the entire image is empty we need to set it to 100% (1.0).