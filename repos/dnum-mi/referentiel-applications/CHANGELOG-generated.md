## Changelog : referentiel-applications (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité (RGAA), la performance de la recherche d'applications, l'ajout de nouvelles fonctionnalités comme la gestion des licences et des stacks techniques, ainsi que des corrections de bugs et des améliorations de la sécurité. L'importation de données via Excel a également été améliorée.

### Évolutions fonctionnelles
- Ajout de la gestion des licences et des stacks techniques sur la fiche d'application.
- Implémentation de filtres de conformité.
- Possibilité d'importer des acteurs depuis un fichier Excel.
- Importation Excel des onglets applications et hébergements.
- Amélioration de l'importation Excel avec la gestion des droits d'accès par application.
- Ajout de la possibilité de trier les types d'acteur.
- Implémentation de la recherche full-text des applications.
- Ajout de la possibilité de s'impersonner en tant qu'un autre utilisateur (pour les administrateurs).
- Ajout de la gestion des tokens applicatifs pour l'administration.
- Amélioration de la représentation graphique MDIT.
- Ajout de la possibilité d'attacher une organisation MAIA lors de la création d'un utilisateur.

### Évolutions techniques
- Optimisation de la performance de la recherche d'applications.
- Correction des alertes de sécurité Dependabot (frontend et backend).
- Mise à jour de l'image Docker frontend pour résoudre des problèmes de permissions.
- Refactoring du code TypeScript pour corriger des anomalies détectées par SonarQube.
- Activation de la configuration ESLint flat.
- Amélioration de la gestion des promesses pour éviter des erreurs.
- Utilisation d'éléments natifs plutôt que de rôles ARIA dans les composants Vue pour améliorer l'accessibilité.
- Amélioration de la gestion des tests E2E (Playwright) avec l'ajout de protocoles de non-régression.
- Correction de problèmes de focus et de gestion du clavier pour l'accessibilité (RGAA).
- Amélioration de la gestion des messages d'état pour l'accessibilité (RGAA).
- Ajout de la gestion des champs obligatoires et des suggestions pour les formulaires (RGAA).

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur et les tests E2E.
- Mise à jour des URLs Swagger pour l'authentification OIDC.
- Amélioration de la documentation et des commentaires.
- Correction de problèmes de responsive design pour le graphique TIME.
- Ajout de tests de non-régression pour plusieurs domaines.
- Correction de problèmes liés à la validation des filtres d'applications.
- Correction de bugs liés à l'historique des modifications de la matrice des droits.
- Correction de problèmes liés à l'affichage du total MDIT.
- Ajout de la possibilité de rendre le champ "date de statut" optionnel.
- Ajout de la validation de l'email MAIA lors de la modification d'un utilisateur.
- Correction de problèmes de localisation des éléments dans les tests E2E.
- Correction de problèmes de déconnexion automatique.
- Correction de problèmes liés à l'affichage des étiquettes de champs manquantes (RGAA).
- Ajout de la gestion des combobox accessibles (RGAA).
- Correction de problèmes liés aux liens et aux mentions de nouvelles fenêtres (RGAA).
- Correction de problèmes liés à l'en-tête, au pied de page et aux repères (landmarks) (RGAA).
- Correction de problèmes liés à la transcription et à l'étiquetage des graphiques (RGAA).
