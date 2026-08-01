## Changelog : sante-psy (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur et la correction de bugs. Les étudiants peuvent désormais télécharger leurs certificats, et des améliorations ont été apportées à la gestion des informations personnelles et à l'annuaire des psychologues. Des corrections ont également été apportées pour empêcher les psychologues de créer des rendez-vous avec des dates incorrectes.

### Évolutions fonctionnelles
- **Espace étudiant :** Possibilité de télécharger des certificats. [#870](https://github.com/betagouv/sante-psy/issues/870)
- **Espace étudiant :** Amélioration de la mise à jour des données personnelles. [#869](https://github.com/betagouv/sante-psy/issues/869)
- **Annuaire :** Amélioration de la formulation du message de suppression de région. [#867](https://github.com/betagouv/sante-psy/issues/867)
- **Annuaire :** Suppression de `addressObject` des paramètres d'URL pour simplifier l'utilisation.
- **Prise de rendez-vous :** Les psychologues ne peuvent plus créer de nouveaux rendez-vous si la date n'a pas été modifiée. [#866](https://github.com/betagouv/sante-psy/issues/866)
- **Support :** Amélioration de la formulation du message de contact du support. [#868](https://github.com/betagouv/sante-psy/issues/868)
- **FAQ :** Mise à jour de la formulation de certaines questions fréquentes. [#868](https://github.com/betagouv/sante-psy/issues/868)

### Évolutions techniques
- Correction temporaire pour pallier un problème avec l'API INES.
- Déplacement du code de mise à jour des données de l'étudiant pour des raisons de style.

### Autres changements
- Application des règles de linting pour améliorer la qualité du code.
