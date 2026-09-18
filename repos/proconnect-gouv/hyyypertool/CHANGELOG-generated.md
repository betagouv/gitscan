## Changelog : hyyypertool (30 derniers jours, au 14 septembre 2026)

### Résumé
Les récentes évolutions permettent une gestion plus rapide des organisations grâce à la création massive par numéro SIRET. La précision du système est également renforcée par un meilleur filtrage des domaines de messagerie approuvés. Parallèlement, l'infrastructure technique a été modernisée pour améliorer l'expérience de développement et la modularité du projet.

### Évolutions fonctionnelles
- Ajout de la création massive d'organisations via le numéro SIRET [#1762](https://github.com/proconnect-gouv/hyyypertool/issues/1762)
- Optimisation de la gestion des domaines : la fonction de récupération ne retourne désormais que les domaines d'e-mails approuvés [#1782](https://github.com/proconnect-gouv/hyyypertool/issues/1782)

### Évolutions techniques
- **Architecture** : Extraction du thème Tailwind DSFR dans un package workspace dédié pour une meilleure modularité [#1791](https://github.com/proconnect-gouv/hyyypertool/issues/1791)
- **Infrastructure & Runtime** : 
    - Mise à jour de l'environnement d'exécution Bun (passage à la version 1.4.2) [#1790](https://github.com/proconnect-gouv/hyyypertool/issues/1790)
    - Mise à jour de la version Node.js [#1771](https://github.com/proconnect-gouv/hyyypertool/issues/1771)
- **Expérience développeur** : Introduction d'un Nix flake pour permettre un environnement de développement sans privilèges sudo [#1783](https://github.com/proconnect-gouv/hyyypertool/issues/1783)
- **Tests** : Phase d'expérimentation sur Cypress 16 [#1786](https://github.com/proconnect-gouv/hyyypertool/issues/1786)
- **Dépendances** : Mise à jour des dépendances internes du groupe `@proconnect-gouv/*` [#1792](https://github.com/proconnect-gouv/hyyypertool/issues/1792)
