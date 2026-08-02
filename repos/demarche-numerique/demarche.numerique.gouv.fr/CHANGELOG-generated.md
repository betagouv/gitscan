## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la performance, notamment au niveau des requêtes en base de données et de la gestion des images. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant les pièces jointes, les champs France Connect et l'export des données. Plusieurs refactorisations ont été effectuées pour préparer le terrain à de futures évolutions et améliorer la maintenabilité du code. L'interface utilisateur a également été améliorée, notamment avec l'intégration de nouveaux composants et la correction de problèmes d'accessibilité.

### Évolutions fonctionnelles
- **France Connect:** Ajout de la gestion des champs AAH, AEEH et étudiant boursier, avec affichage des données et gestion des pièces justificatives.
- **API:** Ajout d'une nouvelle API pour les données ARS.
- **Export de données:** Amélioration de la gestion des noms de fichiers lors de l'export des pièces jointes.
- **Notifications:** Amélioration de l'affichage des notifications de nouveaux messages.
- **Interface administrateur:**
    - Ajout d'un tableau de bord pour suivre l'activité des procédures.
    - Amélioration de l'interface de gestion des modèles d'emails.
- **Géolocalisation:** Amélioration de l'affichage des parcelles sur la carte cadastrale.

### Évolutions techniques
- **Performance:** Optimisation des requêtes en base de données pour améliorer la vitesse de chargement des pages et des données.
- **Refactoring:**
    - Migration de nombreux composants HAML vers ERB pour une meilleure maintenabilité.
    - Refactorisation du code lié à la gestion des champs et des types de champs.
    - Simplification du code lié à la gestion des pièces jointes.
- **Tests:**
    - Ajout de nouveaux tests pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
    - Amélioration de la couverture des tests existants.
- **Dépendances:** Mise à jour de plusieurs dépendances, notamment GraphQL, view_component et css_parser.
- **Rails 8:** Finalisation de la migration vers Rails 8.
- **Sécurité:** Amélioration de la gestion des erreurs et des exceptions.
- **CI/CD:** Amélioration du pipeline CI/CD pour une meilleure automatisation des tests et des déploiements.
- **Oaken:** Introduction de l'outil Oaken pour la gestion des données de test.

### Autres changements
- **Documentation:** Mise à jour de la documentation pour refléter les dernières modifications.
- **i18n:** Extraction de chaînes de caractères codées en dur vers les fichiers de traduction.
- **Accessibilité:** Amélioration de l'accessibilité de certains composants de l'interface utilisateur.
- **Linting:** Correction de problèmes de linting pour améliorer la qualité du code.
- **Suppression de code obsolète:** Suppression de code obsolète et de dépendances inutiles.
