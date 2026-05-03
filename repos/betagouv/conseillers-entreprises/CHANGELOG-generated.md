## Changelog : conseillers-entreprises (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'accessibilité et de l'interface, ainsi que sur des corrections de bugs et des optimisations techniques. Des améliorations ont été apportées aux statistiques pour les sponsors et à la gestion des emails. La documentation et les processus de contribution ont également été mis à jour.

### Évolutions fonctionnelles
- Ajout d'un questionnaire pour les enquêtes auprès des conseillers [#434](https://github.com/betagouv/conseillers-entreprises/issues/434).
- Amélioration de l'accessibilité du formulaire de sollicitation, notamment en ciblant correctement les champs en cas d'erreur.
- Ajout de nouvelles questions sur la satisfaction des entreprises et intégration des résultats dans les exports. [#4392](https://github.com/betagouv/conseillers-entreprises/pulls/4392)
- Mise à jour de l'adresse email utilisée pour les envois, passant à `entreprises.service-public.gouv.fr`. [#4409](https://github.com/betagouv/conseillers-entreprises/pulls/4409)
- Amélioration de l'affichage des statistiques pour les sponsors, avec une page dédiée et des filtres. [#4410](https://github.com/betagouv/conseillers-entreprises/pulls/4410)
- Ajout d'une validation pour les droits d'accès des sponsors. [#439](https://github.com/betagouv/conseillers-entreprises/pulls/439)

### Évolutions techniques
- Refactorisation du code pour supprimer des éléments inutilisés (support subject, bandeau info). [#4438](https://github.com/betagouv/conseillers-entreprises/pulls/4438), [#4440](https://github.com/betagouv/conseillers-entreprises/pulls/4440)
- Optimisation des requêtes SQL pour améliorer les performances, notamment lors de l'affichage des sollicitations. [#4389](https://github.com/betagouv/conseillers-entreprises/pulls/4389)
- Mise à jour de plusieurs dépendances : stimulus (v3.2.2), addressable (v2.9.0), rack (v3.2.6), lodash (v4.18.1), erb (v6.0.4), rack-session (v2.1.2), follow-redirects (v1.16.0).
- Amélioration de la structure du code et suppression de code dupliqué dans la barre de navigation.
- Refactorisation de la gestion des droits d'accès avec Pundit.
- Utilisation de variables CSS pour une meilleure cohérence des couleurs.
- Ajout d'un code de conduite (Contributor Covenant). [#4327](https://github.com/betagouv/conseillers-entreprises/pulls/4327)

### Autres changements
- Mise à jour de la documentation SEO avec l'ajout de schémas et de méta-données pour améliorer le référencement. [#4414](https://github.com/betagouv/conseillers-entreprises/pulls/4414)
- Corrections de typographie et de formulation dans divers textes.
- Amélioration des tests et de la qualité du code.
- Suppression de code inutilisé et nettoyage général du codebase.
