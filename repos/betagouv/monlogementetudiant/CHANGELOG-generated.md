## Changelog : monlogementetudiant (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'intégration de nouvelles fonctionnalités d'alerte et de communication (envoi d'emails Brevo), ainsi que des corrections et optimisations pour la recherche et la gestion des logements et des utilisateurs. Des améliorations ont également été apportées à la page d'accueil et à la documentation.

### Évolutions fonctionnelles
- Ajout d'une alerte sur la page d'accueil concernant le CROUS [#9d70e10](https://github.com/betagouv/monlogementetudiant/commit/9d70e10).
- Possibilité pour les propriétaires de recevoir un email de bienvenue à la création de leur compte (au lieu d'un lien magique) [#8c9cef7](https://github.com/betagouv/monlogementetudiant/commit/8c9cef7).
- Amélioration de la recherche : la correspondance du nom de la ville est désormais priorisée sur le code postal seul [#1b0052d](https://github.com/betagouv/monlogementetudiant/commit/1b0052d), [#2af6ae4](https://github.com/betagouv/monlogementetudiant/commit/2af6ae4).
- Intégration de la FAQ des propriétaires directement vers Crisp Helpdesk [#a88a848](https://github.com/betagouv/monlogementetudiant/commit/a88a848).
- Désactivation de l'autoconnexion pour les étudiants et affichage d'un message générique lors de l'inscription [#3c8a529](https://github.com/betagouv/monlogementetudiant/commit/3c8a529).
- Ajout d'une URL pour les propriétaires sur la page d'accueil [#d3212b9](https://github.com/betagouv/monlogementetudiant/commit/d3212b9).
- Mise en place d'un système d'alerte pour informer les étudiants de nouvelles offres de logement (infrastructure mise en place et envoi d'emails Brevo) [#7246c16](https://github.com/betagouv/monlogementetudiant/commit/7246c16), [#6d8b1ad](https://github.com/betagouv/monlogementetudiant/commit/6d8b1ad), [#bb79142](https://github.com/betagouv/monlogementetudiant/commit/bb79142), [#d20d74a](https://github.com/betagouv/monlogementetudiant/commit/d20d74a).
- Possibilité pour les administrateurs de réinitialiser le mot de passe des étudiants et d'envoyer un email de confirmation [#f7633b5](https://github.com/betagouv/monlogementetudiant/commit/f7633b5).
- Migration de la FAQ de Crisp vers WordPress [#f097cee](https://github.com/betagouv/monlogementetudiant/commit/f097cee).

### Évolutions techniques
- Amélioration de la réhydratation de l'authentification avec le rôle de l'utilisateur [#007d841](https://github.com/betagouv/monlogementetudiant/commit/007d841).
- Backfill de la base de données utilisateurs pour compléter les contacts Brevo [#bb79142](https://github.com/betagouv/monlogementetudiant/commit/bb79142).
- Script pour importer tous les propriétaires vers Brevo [#859e928](https://github.com/betagouv/monlogementetudiant/commit/859e928).
- Sanityzation de la description des logements avant insertion en base de données [#cd2750b](https://github.com/betagouv/monlogementetudiant/commit/cd2750b).
- Restriction de l'upload de fichiers pour les logements aux propriétaires uniquement [#fce6f89](https://github.com/betagouv/monlogementetudiant/commit/fce6f89).
- Mise à jour de l'import Arpej avec une résidence typée [#186f282](https://github.com/betagouv/monlogementetudiant/commit/186f282).

### Autres changements
- Mises à jour du budget freelance [#a3ee11d](https://github.com/betagouv/monlogementetudiant/commit/a3ee11d).
- Mises à jour des dépenses MLE [#e2d2861](https://github.com/betagouv/monlogementetudiant/commit/e2d2861).
- Corrections de typographie et améliorations de la formulation sur la page d'accueil et dans les textes [#5eb2922](https://github.com/betagouv/monlogementetudiant/commit/5eb2922), [#7472464](https://github.com/betagouv/monlogementetudiant/commit/7472464), [#3910ef9](https://github.com/betagouv/monlogementetudiant/commit/3910ef9).
- Ajout de l'icône du propriétaire cliquable si une URL est disponible [#2190513](https://github.com/betagouv/monlogementetudiant/commit/2190513).
- Ajout de pagination avec des ellipses [#255ffbd](https://github.com/betagouv/monlogementetudiant/commit/255ffbd).
- Correction d'un bug dans les tests E2E [#31648f3](https://github.com/betagouv/monlogementetudiant/commit/31648f3).
- Suppression de l'affichage du titre de l'alerte d'accueil lorsque les dates sont dépassées [#9d130a0](https://github.com/betagouv/monlogementetudiant/commit/9d130a0).
- Mise à jour des badges UX sur les résultats de recherche et les détails du logement [#92f64c5](https://github.com/betagouv/monlogementetudiant/commit/92f64c5).
- Mise à jour de la configuration de Claude [#f8c5d3e](https://github.com/betagouv/monlogementetudiant/commit/f8c5d3e).
- Correction pour n'afficher la disponibilité que sur les logements non CROUS [#43f45c4](https://github.com/betagouv/monlogementetudiant/commit/43f45c4).
