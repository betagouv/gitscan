## Changelog : regles.data.gouv.fr (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois a été marqué par une montée en maturité importante de l'interface et des capacités d'extension du projet. Le catalogue de règles est désormais plus riche et visuellement adaptable (thèmes DSFR ou marque blanche), tandis que les outils pour les développeurs ont été considérablement améliorés pour permettre l'extension du site et une meilleure intégration des données.

### Évolutions fonctionnelles
- **Personnalisation de l'interface :** Support du rendu multi-thèmes permettant d'afficher le site soit avec l'identité DSFR, soit en "marque blanche" [#29].
- **Amélioration de l'expérience utilisateur :** Ajout d'un en-tête stylisé [#37], de pages dédiées à l'identité de l'État [#42] et génération automatique du catalogue de règles sous forme de pages statiques [#26].
- **Enrichissement des données :** Intégration de nouveaux enregistrements convertis depuis le format JSON-LD [#38].
- **Extensibilité :** Possibilité pour les projets tiers d'ajouter leurs propres liens de navigation lorsqu'ils étendent le site DSFR [#50].

### Évolutions techniques
- **Moteur de données (Core) :** 
    - Automatisation de la construction du registre à partir des fichiers d'enregistrements avec détection automatique des doublons [#25].
    - Dérivation automatique des types d'enregistrements à partir du schéma de contrat [#23].
    - Publication du registre sous forme de fichier JSON statique pour faciliter la consommation externe [#36].
    - Publication du "core" sous forme d'archive attachée aux releases [#48].
- **Architecture Web :** 
    - Création dynamique des routes à partir de fichiers de configuration dédiés [#39].
    - Mise à disposition de la couche web pour permettre l'extension par d'autres projets Nuxt [#49].
- **CI/CD et Qualité :** 
    - Renforcement des workflows et mise à jour de Nuxt [#52].
    - Mise en place de prévisualisations automatiques des sites sur GitHub Pages [#30].
    - Ajout de tests d'accessibilité (E2E) pour garantir la conformité des sites générés [#51].
    - Intégration de tests et de linting automatisés via `mise run check` [#22].
- **Infrastructure :** Mise à jour de l'environnement de build (Node.js [#44]).
