## Changelog : sante-psy (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, la correction de bugs et l'amélioration de la recherche dans l'annuaire des professionnels de santé. Des restrictions ont été ajoutées pour l'affichage des professionnels dans l'annuaire en fonction de leur convention et de leur université. La connexion et la gestion des tokens ont également été améliorées.

### Évolutions fonctionnelles
- **Annuaire :** Amélioration de la recherche avec l'ajout d'une autocomplétion pour la localisation [#763](https://github.com/betagouv/sante-psy/issues/763).
- **Annuaire :** Les professionnels qui n'ont pas signé de convention ou qui ne sont pas affiliés à une université ne sont plus affichés dans l'annuaire [#823](https://github.com/betagouv/sante-psy/issues/823).
- **Connexion :** Correction d'un problème lié à la connexion et à la gestion des tokens [#829](https://github.com/betagouv/sante-psy/issues/829).
- **API Annuaire :** Mise à jour de l'URL de l'API annuaire pour corriger une dépréciation [#822](https://github.com/betagouv/sante-psy/issues/822).

### Évolutions techniques
- **Sécurité :** Blocage des adresses IP malveillantes [#825](https://github.com/betagouv/sante-psy/issues/825).
- **Sécurité :** Ajout de `crisp.help` à la Content Security Policy (CSP) [#819](https://github.com/betagouv/sante-psy/issues/819).

### Autres changements
- Mise à jour de la dépendance `axios` vers la version 1.15.0 [#827](https://github.com/betagouv/sante-psy/issues/827).
