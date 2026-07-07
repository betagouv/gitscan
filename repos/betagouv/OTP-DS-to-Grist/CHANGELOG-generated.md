## Changelog : OTP-DS-to-Grist (30 derniers jours, au 2 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des configurations de synchronisation, notamment la possibilité de gérer plusieurs configurations simultanément et d'améliorer l'expérience utilisateur lors de leur création et sauvegarde. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Possibilité de gérer plusieurs configurations de synchronisation avec l'API OTP. [#309](https://github.com/betagouv/OTP-DS-to-Grist/issues/309)
- Ajout de la possibilité de supprimer plusieurs configurations simultanément. [#373](https://github.com/betagouv/OTP-DS-to-Grist/issues/373)
- Implémentation du statut de synchronisation même sans configuration définie. [#324](https://github.com/betagouv/OTP-DS-to-Grist/issues/324)
- Amélioration de la gestion des erreurs et affichage de messages plus clairs. [#315](https://github.com/betagouv/OTP-DS-to-Grist/issues/315)
- Possibilité de charger une configuration existante. [#372](https://github.com/betagouv/OTP-DS-to-Grist/issues/372)
- Possibilité de sauvegarder une seule configuration. [#371](https://github.com/betagouv/OTP-DS-to-Grist/issues/371)
- Ajout d'un volet dédié à la gestion des configurations dans l'interface utilisateur. [#362](https://github.com/betagouv/OTP-DS-to-Grist/issues/362) et [#358](https://github.com/betagouv/OTP-DS-to-Grist/issues/358)
- Correction d'un bug empêchant la suppression de la table répétable générique. [#347](https://github.com/betagouv/OTP-DS-to-Grist/issues/347)
- Correction d'un bug lié à la troncature des valeurs de texte trop longues. [#381](https://github.com/betagouv/OTP-DS-to-Grist/issues/381) et [#383](https://github.com/betagouv/OTP-DS-to-Grist/issues/383)

### Évolutions techniques
- Modification du paramètre `max_length` dans la fonction `normalize_column_name` pour une meilleure gestion des noms de colonnes. [#355](https://github.com/betagouv/OTP-DS-to-Grist/issues/355)
- Installation de Vue.js et de DSFR pour l'interface utilisateur. [#328](https://github.com/betagouv/OTP-DS-to-Grist/issues/328) et [#342](https://github.com/betagouv/OTP-DS-to-Grist/issues/342)

### Autres changements
- Mise à jour de la documentation et du tutoriel. [#346](https://github.com/betagouv/OTP-DS-to-Grist/issues/346)
- Correction de chemin du manifest et mise à jour de l'interface Vue.js.
- Diverses mises à jour de dépendances (urllib3, form-data, ruff, pytest, cryptography, baseline-browser-mapping, eslint, python-socketio, sqlalchemy). Ces mises à jour sont de maintenance et n'impactent pas directement l'utilisateur.
