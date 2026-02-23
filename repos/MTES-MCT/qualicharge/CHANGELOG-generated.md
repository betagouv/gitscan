## Changelog : qualicharge (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à qualicharge au cours des 30 derniers jours. Les mises à jour incluent des corrections de bugs dans les workflows de supervision de la recharge, des améliorations de la gestion des données, et des mises à jour régulières des dépendances pour assurer la sécurité et la stabilité du système. Une nouvelle version de l'API a également été publiée.

### Évolutions fonctionnelles
- Correction d'un bug dans l'indicateur de qualité PDCM dans les workflows Prefect. (#50bfa31)
- Prise en compte des points de recharge hors service dans les vérifications de refroidissement des données. (#aacb98a)
- Correction de l'unité de mesure de l'énergie envoyée par CARBURE. (#45bba03)
- Amélioration du flux TIRUERT vers CARBURE pour une meilleure performance. (#40547e6)
- Publication de la version 0.32.0 de l'API, incluant des corrections pour la gestion des dates et heures. (#6f76b05, #af8d0f0)

### Évolutions techniques
- Refactorisation des flux de refroidissement pour une meilleure maintenabilité. (#2a9556e)
- Activation des linters pour tous les modules du projet afin d'améliorer la qualité du code. (#c1a254c)
- Les champs de date et d'heure `Status` et `Session` sont maintenant forcés à être "TZ-aware" pour une gestion correcte des fuseaux horaires. (#af8d0f0)
- Amélioration de la gestion des erreurs et possibilité d'échouer plus tôt dans les flux de refroidissement. (#08aa38b)

### Autres changements
- Mise à jour de plusieurs dépendances et images Docker (uv, metabase, locust, terraform, python-multipart, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance. (#36340ca, #ee69550, #e02a46d, #57e08d0, #fa4f1f9, #295f0e6, #6e9ab49, #4f7b703, #0387bd4, #61bdfba, #dad799d, #f4564ba, #c95494d, #213752b, #909615c, #41fd1b0, #e6234d5, #19b3802, #55f144c, #4855c7d, #56c7716, #6de1d64, #0bb9208, #a30d80e, #60bf406, #7c4a26a)
- Mise à jour des actions GitHub (checkout, setup-python) pour bénéficier des dernières fonctionnalités. (#60bf406, #7c4a26a)
- Actualisation des indicateurs pour les attentes de qualité Prefect. (#af312f5)
