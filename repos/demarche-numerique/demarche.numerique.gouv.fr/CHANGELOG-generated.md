## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans l'expérience utilisateur avec l'introduction de la personnalisation des listes de dossiers. Les usagers peuvent désormais choisir les informations qu'ils souhaitent voir apparaître en priorité dans leurs tableaux de bord. Parallèlement, des améliorations significatives ont été apportées à la recherche, à la cartographie et à l'accessibilité, tout en profitant d'une refonte technique profonde visant à rendre l'outil plus rapide, plus robuste et plus facile à maintenir.

### Évolutions fonctionnelles
- **Personnalisation de l'affichage des dossiers** : Les utilisateurs peuvent désormais personnaliser les colonnes affichées dans leur liste de dossiers, avec la possibilité de regrouper les champs par sections, de gérer les champs obligatoires et d'afficher directement les valeurs sélectionnées. [#13373](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13373)
- **Amélioration de l'éditeur et des tags** : Ajout d'une légende pour les tags dans l'éditeur, prise en charge des couleurs et des suffixes pour les tags conditionnels, et affichage systématique des indices de valeurs vides. [#13510](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13510)
- **Recherche et Cartographie** : 
    - Amélioration de la recherche plein texte dans les dossiers pour des résultats plus pertinents.
    - Intégration de cartes statiques dans les exports PDF des dossiers pour une meilleure traçabilité géographique.
    - Correction des couches cartographiques (cadastres et RPG) pour éviter les conflits d'affichage.
- **Administration et Statistiques** : 
    - Intégration de nouveaux flux de données pour l'endpoint ARS. [#13573](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13573)
    - Mise à jour du calcul des statistiques pour refléter précisément le nombre de dossiers réellement soumis à l'administration.
- **Accessibilité (A11y)** : Amélioration de l'expérience pour les utilisateurs de lecteurs d'écran, notamment via une meilleure gestion des notifications et des attributs d'images.

### Évolutions techniques
- **Refactoring majeur du système de champs** : Migration de la logique des types de champs vers une architecture polymorphe (Single Table Inheritance), permettant une gestion plus propre et évolutive des comportements spécifiques à chaque type de champ. [#13662](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13662)
- **Modernisation de l'interface utilisateur** : Remplacement des bibliothèques d'icônes et de composants par `react-aria-components` et les icônes officielles du DSFR.
- **Optimisation des performances** : 
    - Segmentation du trafic GraphQL pour une meilleure observabilité via Skylight.
    - Optimisation de la recherche via l'utilisation de vecteurs de recherche (tsvectors) en base de données.
    - Amélioration des temps de réponse sur les listes de dossiers et les requêtes GraphQL complexes.
- **Tests et Qualité** : Migration des tests système de Selenium/Chrome vers Playwright pour une exécution plus rapide et plus stable. [#13504](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13504)
- **Nettoyage de l'infrastructure** : Suppression du support de `delayed_job` pour simplifier la gestion des tâches de fond. [#13682](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13682)
- **Sécurité et Robustesse** : 
    - Renforcement du traitement des images et de la gestion des fichiers téléchargés (uploads).
    - Durcissement de la gestion des erreurs pour éviter les fuites d'informations techniques.

### Autres changements
- Migration massive de templates de vues de HAML vers ERB pour uniformiser le code.
- Mise à jour de la documentation de la FAQ avec de nouvelles captures d'écran.
