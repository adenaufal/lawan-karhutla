# Lawan Karhutla

Situs foto profil ala twibbon untuk kampanye #LawanKarhutla. Unggah foto, pilih filter, lalu unduh hasilnya untuk dipasang di foto profil.

**Coba di sini:** https://lawankarhutla.pages.dev

Filternya meniru warna langit Palangka Raya, Kalimantan Tengah, saat tertutup asap kebakaran hutan dan lahan pada Oktober 2026. Judul situsnya "Ini bukan filter" karena warna oranye itu memang warna langit di sana.

## Kenapa situs ini dibuat

Asap karhutla sudah menyelimuti Palangka Raya sejak akhir Juli 2026. Pertengahan Oktober, ISPU kota itu sempat tercatat 1.294, padahal kategori berbahaya dimulai di angka 300. Per 11 Oktober, Kementerian Kesehatan mencatat 62.400 balita kena ISPA di daerah terdampak. Asapnya juga sampai ke Malaysia, Singapura, Brunei, dan Timor-Leste. Di Johor dan Timor-Leste, sekolah sampai diliburkan.

Ganti foto profil saja tidak memadamkan api. Kami membuat situs ini supaya orang yang jauh dari asap ikut melihat warnanya, membaca angkanya, lalu ikut mengawal penyelidikan terhadap 95 perusahaan yang sedang diperiksa polisi.

## Cara pakai

1. Buka situsnya, lalu pilih foto atau tarik foto ke lingkaran. Rasio apa saja bisa dipakai, nanti dipotong jadi persegi.
2. Geser foto untuk mengatur posisi, dan pakai slider "Perbesar" kalau wajah terlalu kecil.
3. Pilih gaya filter, lalu atur kekuatannya.
4. Klik "Unduh foto". Hasilnya PNG 1080×1080.
5. Klik "Salin caption untuk postinganmu" kalau mau sekalian posting.

Pesan kampanye di foto ("INI BUKAN FILTER", "LAWAN KARHUTLA", #LawanKarhutla) bisa dimatikan. Posisinya sudah diatur agar tidak terpotong saat platform memotong foto profil jadi lingkaran.

## Gaya filter

| Gaya | Hasilnya |
|---|---|
| Asap | Oranye kekuningan yang datar, tanpa hitam pekat. Paling mirip foto langit Palangka Raya. |
| Duotone | Gradasi api dari hitam bara ke merah lalu kuning, dengan kontras keras. |
| Aberasi | Warna Asap ditambah pergeseran kanal merah dan biru yang makin kuat ke pinggir foto. |
| Campuran | Duotone, aberasi, dan grain kasar. Paling dramatis. |

## Privasi

Foto diproses di browser memakai Canvas API. Tidak ada server, tidak ada unggahan, dan tidak ada analitik. Satu-satunya permintaan ke luar adalah font Inter dari Google Fonts.

## Menjalankan di komputer sendiri

Situs ini cuma satu file HTML tanpa build step dan tanpa dependensi.

```bash
git clone https://github.com/adenaufal/lawan-karhutla.git
cd lawan-karhutla
python -m http.server 8000 --directory public
```

Lalu buka http://localhost:8000. Membuka `public/index.html` langsung dari file juga bisa.

## Deploy

Situs ini di-host di Cloudflare Pages. Untuk deploy ulang:

```bash
npx wrangler pages deploy public --project-name lawankarhutla --branch main
```

Folder `public` juga bisa diunggah ke hosting statis lain seperti Netlify, Vercel, atau GitHub Pages.

## Struktur

```
public/
  index.html   # seluruh situs: markup, gaya, dan logika filter
```

Kalau mau mengubah warna filter, cari `HAZE_LUT` dan `FIRE_LUT` di `index.html`. Pengaturan tiap gaya (kontras, aberasi, vignette, grain) ada di objek `MODES`.

## Sumber data

Angka di situs dan README ini diambil dari berita per pertengahan Oktober 2026. ISPU berubah tiap jam, jadi cek sumber terbaru sebelum mengutip.

- [ANTARA Kalteng: kabut asap masih menyelimuti Palangka Raya](https://kalteng.antaranews.com/berita/845510/kabut-asap-dampak-karhutla-masih-menyelimuti-palangka-raya)
- [detikHealth: 62 ribu balita alami ISPA di wilayah terdampak karhutla](https://health.detik.com/berita-detikhealth/d-8709190/62-ribu-balita-alami-ispa-di-wilayah-terdampak-karhutla)
- [Kompas: kabut asap dari Indonesia ganggu Malaysia dan Singapura](https://internasional.kompas.com/read/2026/10/15/151532570/kabut-asap-dari-indonesia-ganggu-malaysia-dan-singapura-asean-turun)
- [Wikipedia: 2026 Southeast Asian haze](https://en.wikipedia.org/wiki/2026_Southeast_Asian_haze)

## Kontribusi

Issue dan pull request terbuka. Yang paling membantu saat ini: koreksi angka dengan sumber resmi (KLH, Kemenkes, Polri), terjemahan bahasa Inggris dan Melayu untuk pembaca dari negara tetangga, dan uji tampilan di berbagai ponsel.

## Tentang inisiasi ini

Diinisiasi oleh [@adenaufal](https://x.com/adenaufal) dan [@bejowish](https://x.com/bejowish).

## Lisensi

[MIT](LICENSE)
