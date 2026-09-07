## Changelog : docs (30 derniers jours, au 2026-09-04)

### Résumé
Ce mois-ci, la suite a considérablement enrichi ses capacités d'édition avec l'ajout de blocs mathématiques et de diagrammes, ainsi que de nouveaux outils de recherche et d'exportation PDF. Les efforts se sont également concentrés sur l'amélioration de l'accessibilité, l'optimisation des performances du backend et la modernisation de l'interface utilisateur.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** : Ajout de blocs de mathématiques et de diagrammes, fonction de recherche et remplacement, compteur de mots et possibilité de copier un lien direct vers un bloc.
- **Expérience utilisateur** : Exportation de présentations en PDF (avec filigrane), tri des documents par nom, déplacement de fichiers et passage du système de favoris aux "étoiles".
- **Accessibilité** : Amélioration de la navigation au clavier (interliens), annonce des états de chargement pour les lecteurs d'écran et gestion globale des styles de focus.
- **Corrections** : Résolution de bugs concernant les blocs de code, l'exportation d'images, la duplication de documents vides et l'affichage des options de session pour les utilisateurs non authentifiés.

### Évolutions techniques
- **Architecture & Refactoring** : Migration vers Blocknote 0.54.0, remplacement de `ui-kit` par `ui-components` et suppression de la dépendance `whitenoise`.
- **Performance** : Optimisation de l'utilisation CPU et des requêtes SQL pour l'authentification des médias, et passage au "throttling" réactif pour l'interface.
- **Infrastructure & Backend** : Configuration de la limite de mémoire d'upload, support asynchrone pour les middlewares personnalisés et corrections sur les déploiements Helm et Keycloak.
- **Qualité & Sécurité** : Stabilisation des tests E2E, ajout de la couverture de tests pour l'export PDF et correction de vulnérabilités JS.

### Autres changements
- **Internationalisation** : Ajout de la langue polonaise et mise à jour des chaînes de traduction.
- **Design** : Mise à jour des logos et modernisation des assets d'onboarding (passage aux formats webm et webp).
