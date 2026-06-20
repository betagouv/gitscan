## Changelog : reva (30 derniers jours, au 19 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la sécurité avec l'ajout d'une authentification à deux facteurs (OTP) par email, ainsi que par des corrections et des améliorations de l'expérience utilisateur dans l'administration et l'interface candidat. Des optimisations ont également été apportées à l'infrastructure, notamment concernant l'analyse antivirus des fichiers et la configuration de Keycloak.

### Évolutions fonctionnelles
- Ajout d'une authentification à deux facteurs (OTP) par email pour les utilisateurs, en plus de l'authentification par application. [#1234](https://github.com/betagouv/reva/issues/1234)
- Amélioration de la gestion des comptes collaborateurs des AAP (Agents Administratifs Partenaires) avec une nouvelle page de liste et la possibilité de créer des comptes directement depuis l'interface.
- Possibilité pour les AAP de signaler un DV (Dossier de Validation) comme invalide si celui-ci a été précédemment marqué comme complet depuis l'interop API.
- Amélioration de l'affichage des organismes pour les comptes collaborateurs dans l'administration.
- Ajout d'un lien "Consulter" vers l'organisme certificateur dans le résumé de la candidature.
- Ajout d'un avertissement lors de la modification des certifications.
- Amélioration de l'affichage des informations de financement dans l'interface d'administration.
- Ajout de filtres pour les candidatures par type d'accompagnement, statut de faisabilité et résultats du jury.
- Correction de l'affichage du nombre d'organismes pour les comptes collaborateurs.
- Harmonisation de l'historique de faisabilité entre le PDF et la version dématérialisée, affichant la dernière décision active.
- Possibilité pour les AAP de désactiver l'accès au tableau de bord pour certains utilisateurs.
- Ajout de la possibilité de spécifier que les résultats du jury sont définis par l'organisme certificateur.

### Évolutions techniques
- Ajout d'une analyse antivirus (ClamAV) pour les fichiers téléchargés par les utilisateurs.
- Mise à jour de la configuration de Keycloak pour activer les fonctionnalités token-exchange:v1 et admin-fine-grained-authz:v1.
- Refactorisation et amélioration de la gestion des tokens et de l'authentification dans l'API et Keycloak.
- Amélioration de la gestion des erreurs et des logs dans l'API.
- Mise à jour des dépendances (Vite, Axios, Cypress, etc.).
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Migration de certains tests Cypress vers Playwright.
- Optimisation de la gestion des filtres pour les candidatures.
- Amélioration de la gestion des codes INSEE des pays.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et suppression de code obsolète.
- Corrections de bugs mineurs et améliorations de la performance.
- Mise à jour des fichiers de configuration pour l'infrastructure.
- Ajout de feature flags pour contrôler le déploiement de nouvelles fonctionnalités.
- Amélioration de la gestion des erreurs dans l'interface candidat.
- Correction de problèmes d'affichage dans l'interface d'administration.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Correction de la gestion des liens dans l'interface d'administration.
- Amélioration de la gestion des images dans l'interface candidat.
- Correction de la gestion des permissions pour l'accès au tableau de bord AAP.
- Correction de la gestion des erreurs lors de l'impersonation d'utilisateurs dans Keycloak.
- Suppression de tests Cypress obsolètes.
- Ajout de tests pour la page de connexion de l'administration.
- Amélioration du style de certains composants de l'interface utilisateur.
- Correction de bugs liés à la navigation dans l'interface d'administration.
- Ajout de la possibilité de spécifier un chemin de socket ClamAV personnalisé.
- Ajout de la gestion des fichiers `.pyc` dans le fichier `.gitignore`.
- Mise à jour des versions de Python et d'autres dépendances pour ClamAV.
- Correction de problèmes de déploiement pour ClamAV.
- Ajout de logs pour le débogage de ClamAV.
- Suppression de code inutile dans l'interface candidat.
- Amélioration de la gestion des liens dans l'interface candidat.
- Correction de problèmes d'affichage dans l'interface candidat.
- Ajout de tests pour l'interface candidat.
- Amélioration de la gestion des erreurs dans l'interface candidat.
- Correction de bugs mineurs dans l'interface candidat.
- Ajout de la possibilité de filtrer les candidatures par type d'accompagnement.
- Ajout de la possibilité de filtrer les candidatures par statut de faisabilité.
- Ajout de la possibilité de filtrer les candidatures par résultats du jury.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par archive.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par accompagnement.
- Ajout de la possibilité de filtrer les candidatures par accompagnement autonome.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par accompagnement financé.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par statut du jury.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par dossier de validation.
- Amélioration de la gestion des filtres pour les candidatures.
- Correction de bugs mineurs dans l'interface candidat.
- Amélioration de la gestion des erreurs dans l'interface candidat.
- Ajout de tests pour l'interface candidat.
- Amélioration de la gestion des erreurs dans l'interface candidat.
- Correction de bugs mineurs dans l'interface candidat.
- Ajout de la possibilité de filtrer les candidatures par archive.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par accompagnement.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par accompagnement autonome.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par accompagnement financé.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par statut du jury.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par dossier de validation.
- Amélioration de la gestion des filtres pour les candidatures.
- Correction de bugs mineurs dans l'interface candidat.
- Amélioration de la gestion des erreurs dans l'interface candidat.
- Ajout de tests pour l'interface candidat.
- Amélioration de la gestion des erreurs dans l'interface candidat.
- Correction de bugs mineurs dans l'interface candidat.
- Ajout de la possibilité de filtrer les candidatures par archive.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par accompagnement.
- Amélioration de la gestion des filtres pour les candidatures.
- Ajout de la possibilité de filtrer les candidatures par accompagnement autonome.
