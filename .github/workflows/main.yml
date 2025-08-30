jobs:
  post:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Get LinkedIn Person URN
        env:
          LINKEDIN_TOKEN: ${{ secrets.LINKEDIN_TOKEN }}
        run: |
          curl -H "Authorization: WPL_AP1.ECHSF2QQziCrdZSs.CeCPew==" \
               -H "X-Restli-Protocol-Version: 2.0.0" \
               https://api.linkedin.com/v2/me
