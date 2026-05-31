name: GEMA-OPERASI-CUAN-V1
on: [push, workflow_dispatch]

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: 'true'

jobs:
  eksekusi_intelijen:
    runs-on: ubuntu-latest
    steps:
      - name: "1. Mengambil Markas Pusat"
        uses: actions/checkout@v4

      - name: "2. Menyiapkan Lingkungan Python"
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: "3. EKSEKUSI KEKUASAAN TOTAL PT GEMA"
        run: |
          echo "========================================="
          echo "LAPOR BOSS ALDI RAFA!"
          echo "SISTEM PT GEMA AMAN DAN SADAR!"
          echo "========================================="
          python otak_gema_ai.py
          python gema_chip_supremasi.py
          python gema_intel_upgrade_31.py
          python gema_dewa_omega_v99.py
          python gema_nurani_supradewa.py
