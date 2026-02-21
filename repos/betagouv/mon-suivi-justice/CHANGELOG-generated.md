## Changelog : mon-suivi-justice (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours d'évolution du service mon-suivi-justice. La période a été principalement marquée par des mises à jour de dépendances afin de maintenir la sécurité et la stabilité de l'application. Une correction concernant l'intégration continue a également été apportée.

### Évolutions fonctionnelles
- Correction d'un problème dans la chaîne d'intégration continue (#1408, #1414).

### Évolutions techniques
- Mise à jour de nombreuses dépendances Ruby et JavaScript (voir section "Autres changements" pour la liste complète).
- Mise à jour de la version de Rails (ActionCable, Actiontext, Activestorage) vers la version 8.1.200 (#1382, #1381, #1380).
- Mise à jour de la gem pg vers la version 1.6.3 (#1379).

### Autres changements
- Mises à jour de dépendances :
    - faraday (2.14.0 -> 2.14.1) (#1408)
    - spring (4.4.0 -> 4.4.2) (#1405)
    - esbuild (0.27.0 -> 0.27.2, puis 0.27.3) (#1370, #1404)
    - faker (3.5.2 -> 3.5.3, puis 3.6.0) (#1361, #1402)
    - rack (3.2.4 -> 3.2.5) (#1414)
    - autoprefixer (10.4.23 -> 10.4.24) (#1394)
    - date-holidays (3.26.5 -> 3.26.8) (#1396)
    - lodash (4.17.21 -> 4.17.23) (#1390)
    - listen (3.9.0 -> 3.10.0) (#1388)
    - state_machines-graphviz (0.0.2 -> 0.1.0) (#1383)
    - trix (2.1.15 -> 2.1.16) (#1377)
    - uri (1.0.3 -> 1.0.4) (#1376)
    - faraday-retry (2.3.2 -> 2.4.0) (#1374)
    - @gouvfr/dsfr (1.14.2 -> 1.14.3) (#1368)
    - debug (1.11.0 -> 1.11.1) (#1367)
    - tzinfo-data (1.2025.2 -> 1.2025.3) (#1364)
    - dotenv-rails (3.1.8 -> 3.2.0) (#1362)
    - addressable (2.8.7 -> 2.8.8) (#1359)
