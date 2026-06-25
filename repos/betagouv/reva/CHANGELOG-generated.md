## Changelog : reva (30 derniers jours, au 24 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur dans l'espace administrateur, notamment sur les pages de gestion des candidatures et des profils. Des corrections et des optimisations ont également été apportées aux API, notamment en matière de sécurité (analyse antivirus des fichiers) et de gestion des OTP (One-Time Password) pour une authentification renforcée. L'ajout de nouvelles fonctionnalités, comme la gestion des comptes collaborateurs AAP et l'intégration de ClamAV pour l'analyse antivirus, renforce la robustesse et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur et de l'expérience utilisateur sur les pages de certification, d'éligibilité, de modification des expériences du candidat et du profil candidat dans l'espace administrateur. [#1037](https://github.com/betagouv/reva/pull/1037)
- Ajout d'une page de sélection des autorités de certification dans l'espace administrateur.
- Ajout d'un lien "Consulter" vers les détails de l'autorité de certification dans le résumé de la candidature.
- Possibilité pour les AAPs d'ajouter de nouveaux comptes collaborateurs depuis la liste des comptes.
- Affichage d'un badge pour les comptes AAP désactivés et désactivation du lien vers la carte.
- Amélioration de l'affichage des raisons d'arrêt d'accompagnement.
- Ajout de filtres pour les candidatures (statut, type d'accompagnement, financement, résultats du jury, etc.) dans la page "candidatures-for-aap".
- Ajout d'une nouvelle raison d'arrêt d'accompagnement.
- Amélioration de la gestion des filtres et de l'affichage des données dans l'espace administrateur.
- Possibilité de renvoyer un code OTP par email.
- Ajout d'une page pour gérer les autorités de certification multiples.
- Amélioration de la gestion des fichiers joints (augmentation de la taille maximale autorisée).
- Remplacement du lien "Contact" par un formulaire de pré-qualification sur le site web.
- Correction de l'affichage des lieux de naissance.
- Amélioration de la gestion des erreurs côté client avec Urql.

### Évolutions techniques
- Refactorisation de la logique de détection des feature flags pour les tableaux de bord AAP.
- Optimisation et renforcement des vérifications avant l'envoi des DFF (Dossier de Formation) à l'autorité de certification.
- Ajout d'une analyse antivirus des fichiers téléchargés par les utilisateurs via l'intégration de ClamAV.
- Mise à jour des dépendances (Strapi, Vite, shell-quote, etc.).
- Amélioration de la gestion des tokens persistants dans l'espace administrateur pour l'authentification SSO.
- Ajout d'un endpoint `establish-sso` pour la gestion de l'authentification SSO inter-applications.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Migration de certains tests Cypress vers Playwright.
- Amélioration de la gestion des erreurs et des logs.
- Correction de bugs et optimisations de performance diverses.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et refactoring de certains composants.
- Mise à jour de la configuration de l'infrastructure.
- Ajout de fichiers `.pyc` à `.gitignore`.
- Correction de problèmes liés à la gestion des ports dans l'environnement ClamAV.
- Suppression de tests Cypress obsolètes.
- Correction de problèmes d'affichage et de navigation dans l'interface administrateur.
- Mise à jour des emails d'activation des certifications dans Keycloak.
- Correction de bugs mineurs et améliorations de la qualité du code.
