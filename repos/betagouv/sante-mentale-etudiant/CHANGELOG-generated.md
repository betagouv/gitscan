## Changelog : sante-mentale-etudiant (30 derniers jours, au 2026-04-30)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'internationalisation du site, permettant une meilleure accessibilité pour les utilisateurs francophones et non-francophones. Des corrections et optimisations ont également été apportées à l'interface d'administration et à la gestion des pages, ainsi qu'une simplification du déploiement sur Scalingo.

### Évolutions fonctionnelles
- Ajout d'un sélecteur de langue dans l'interface d'administration pour faciliter la gestion du contenu multilingue. [#464](https://github.com/betagouv/sante-mentale-etudiant/issues/464)
- Internationalisation des champs de formulaire pour une meilleure expérience utilisateur en fonction de la langue sélectionnée. [#481](https://github.com/betagouv/sante-mentale-etudiant/issues/481) et [#473](https://github.com/betagouv/sante-mentale-etudiant/issues/473)
- Amélioration du menu utilisateur avec l'ajout d'une option appropriée. [#3b6f4d2](https://github.com/betagouv/sante-mentale-etudiant/commit/3b6f4d2)
- Correction de l'URL des pages pour assurer un fonctionnement correct de la navigation. [#3733200](https://github.com/betagouv/sante-mentale-etudiant/commit/3733200)
- Correction de l'affichage du header configurable. [#469](https://github.com/betagouv/sante-mentale-etudiant/issues/469)

### Évolutions techniques
- Mise en place d'un déploiement en un clic sur la plateforme Scalingo, simplifiant le processus de publication du site. [#484](https://github.com/betagouv/sante-mentale-etudiant/issues/484)
- Optimisation du panneau de tutoriel dans l'administration. [#473](https://github.com/betagouv/sante-mentale-etudiant/issues/473)
- Correction d'une migration et suppression d'une migration inutile. [#f085b55](https://github.com/betagouv/sante-mentale-etudiant/commit/f085b55) et [#50e8757](https://github.com/betagouv/sante-mentale-etudiant/commit/50e8757)
- Modification du nom d'une variable pour améliorer la cohérence du code. [#15bffb8](https://github.com/betagouv/sante-mentale-etudiant/commit/15bffb8)

### Autres changements
- Ajout de commentaires pour améliorer la lisibilité du code. [#f58d720](https://github.com/betagouv/sante-mentale-etudiant/commit/f58d720)
- Ajout d'un script pour le sélecteur de langue dans l'administration. [#4f787cd](https://github.com/betagouv/sante-mentale-etudiant/commit/4f787cd)
- Ajout d'une gestion des erreurs lors de la validation. [#9fef8cc](https://github.com/betagouv/sante-mentale-etudiant/commit/9fef8cc)
