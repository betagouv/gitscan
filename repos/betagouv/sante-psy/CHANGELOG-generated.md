## Changelog : sante-psy (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, la correction de bugs et l'amélioration de la recherche dans l'annuaire des professionnels. Des corrections ont été apportées pour bloquer des adresses IP malveillantes et pour assurer le bon fonctionnement de l'authentification. L'annuaire a également été mis à jour pour mieux gérer les établissements non conventionnés et pour offrir une recherche de localisation plus performante.

### Évolutions fonctionnelles
- **Annuaire :** Amélioration de la recherche de localisation avec auto-complétion. [#763](https://github.com/betagouv/sante-psy/issues/763)
- **Annuaire :** Les professionnels ne sont plus affichés dans l'annuaire s'il n'y a pas de convention signée avec l'université. [#823](https://github.com/betagouv/sante-psy/issues/823)
- **Authentification :** Correction d'un problème lié à la connexion et à la gestion des tokens. [#829](https://github.com/betagouv/sante-psy/issues/829)

### Évolutions techniques
- **Sécurité :** Blocage d'adresses IP malveillantes pour renforcer la sécurité de l'application. [#825](https://github.com/betagouv/sante-psy/issues/825)
- **Cartographie :** Correction de l'origine des tuiles OpenStreetMap pour éviter des problèmes de sécurité liés au CORS. [#832](https://github.com/betagouv/sante-psy/issues/832)
- **API Annuaire :** Mise à jour de l'URL d'une API annuaire obsolète. [#822](https://github.com/betagouv/sante-psy/issues/822)

### Autres changements
- Mise à jour de la dépendance `axios` en version 1.15.0. [#827](https://github.com/betagouv/sante-psy/issues/827)
