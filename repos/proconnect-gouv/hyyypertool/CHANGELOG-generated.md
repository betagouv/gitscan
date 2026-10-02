## Changelog : hyyypertool (30 derniers jours, au 30 septembre 2026)

### Résumé
Ce mois-ci, hyyypertool a renforcé ses capacités de gestion, notamment avec l'introduction de la création massive d'organisations. Une part importante des travaux a été consacrée à la modernisation de l'infrastructure de tests automatisés afin de garantir une meilleure stabilité et une plus grande fiabilité des fonctionnalités de modération.

### Évolutions fonctionnelles
- Ajout de la création massive d'organisations via les numéros SIRET [#1762](https://github.com/proconnect-gouv/hyyypertool/issues/1762).
- Amélioration de la gestion des domaines : la fonction de récupération des domaines retourne désormais uniquement les domaines de messagerie approuvés [#1782](https://github.com/proconnect-gouv/hyyypertool/issues/1782).
- Correction de la gestion des conversations Crisp pour assurer une transition fluide vers les nouvelles conversations en cas de ticket obsolète [#1800](https://github.com/proconnect-gouv/hyyypertool/issues/1800).

### Évolutions techniques
- **Refonte majeure de la suite de tests E2E** : Migration de l'infrastructure de tests (Cypress et Bunwright) vers un nouveau système basé sur Buncept pour une meilleure stabilité et une syntaxe simplifiée [#1827](https://github.com/proconnect-gouv/hyyypertool/issues/1827). Cela inclut le portage de l'ensemble des scénarios de tests critiques (gestion des membres, navigation, modération, vérification de domaines, etc.) [#1837](https://github.com/proconnect-gouv/hyyypertool/issues/1837), [#1835](https://github.com/proconnect-gouv/hyyypertool/issues/1835), [#1833](https://github.com/proconnect-gouv/hyyypertool/issues/1833).
- **Amélioration de l'expérience développeur** :
    - Mise en place de Nix pour permettre un environnement de développement local simplifié et sans privilèges root [#1783](https://github.com/proconnect-gouv/hyyypertool/issues/1783).
    - Extraction du thème Tailwind DSFR dans un package dédié pour améliorer la modularité du projet [#1791](https://github.com/proconnect-gouv/hyyypertool/issues/1791).
- **Maintenance et infrastructure** :
    - Mise à jour du runtime Bun [#1790](https://github.com/proconnect-gouv/hyyypertool/issues/1790).
    - Mise à jour des dépendances internes de l'écosystème ProConnect [#1792](https://github.com/proconnect-gouv/hyyypertool/issues/1792).
