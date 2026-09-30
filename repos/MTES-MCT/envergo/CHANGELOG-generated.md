## Changelog : envergo (30 derniers jours, au 29 septembre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'expérience de simulation (passage à la version 2) et une amélioration significative de la précision des données réglementaires. L'outil est désormais plus performant dans la gestion et la catégorisation des espèces protégées et des zones réglementées (Natura 2000, sites classés, etc.), tout en offrant une interface plus claire et mieux structurée pour l'utilisateur.

### Évolutions fonctionnelles
- **Nouvelle expérience de simulation (V2) :** Déploiement d'un nouveau parcours utilisateur incluant une nouvelle page d'affichage des résultats et la possibilité de consulter des scénarios alternatifs [#1236](https://github.com/MTES-MCT/envergo/issues/1236), [#1254](https://github.com/MTES-MCT/envergo/issues/1254), [#1255](https://github.com/MTES-MCT/envergo/issues/1255).
- **Amélioration de la gestion réglementaire :** 
    - Optimisation de la catégorisation des espèces et des réglementations (RU, Natura 2000, sites protégés, sites classés, etc.).
    - Meilleure gestion des périodes d'interdiction (AHR) avec l'utilisation de plages de dates.
- **Interface utilisateur (UI) et expérience (UX) :**
    - Refonte de la présentation des espèces : utilisation de tableaux rétractables pour plus de clarté et meilleure organisation des listes.
    - Mise à jour de la navigation : nouveau menu plus intuitif et ajout de filtres par catégorie [#1231](https://github.com/MTES-MCT/envergo/issues/1231).
    - Amélioration de la lisibilité des informations de contact et des libellés (ex: passage de "point d'eau" à "pièce d'eau").
    - Ajout d'informations sur les alignements d'arbres directement sur la page d'accueil.
- **Cartographie :** Ajout d'infobulles (tooltips) sur les cartes et mise à jour du logo Dossier Nature.

### Évolutions techniques
- **Architecture et structure :** 
    - Restructuration profonde des URLs du projet et de l'architecture des pages pour une meilleure maintenance [#1282](https://github.com/MTES-MCT/envergo/issues/1282).
    - Séparation des pages de résumé de projet et de résultats de la "moulinette".
- **Stockage et infrastructure :** 
    - Implémentation complète du stockage sur S3 pour la gestion des fichiers et sécurisation de l'accès aux fichiers privés [#1261](https://github.com/MTES-MCT/envergo/issues/1261).
- **Performances et sécurité :**
    - Optimisation des requêtes de données (HRU) et mise en place d'un système de cache pour la densité [#1266](https://github.com/MTES-MCT/envergo/issues/1266), [#1238](https://github.com/MTES-MCT/envergo/issues/1238).
    - Renforcement de la sécurité des données de statistiques [#1265](https://github.com/MTES-MCT/envergo/issues/1265) et amélioration de l'API d'autorisation [#1244](https://github.com/MTES-MCT/envergo/issues/1244).
- **Qualité logicielle (CI/CD) :** 
    - Ajout d'une vérification automatique des migrations de base de données dans le pipeline d'intégration continue [#1259](https://github.com/MTES-MCT/envergo/issues/1259).

### Autres changements
- **Documentation :** Mise à jour du README concernant les procédures d'anonymisation des données.
- **Maintenance :** Nettoyage important du code (suppression de fichiers et de fonctions obsolètes) et amélioration de la couverture des tests automatisés.
