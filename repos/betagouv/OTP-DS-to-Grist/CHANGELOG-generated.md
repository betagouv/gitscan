## Changelog : OTP-DS-to-Grist (30 derniers jours, au 26 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur la fiabilité de la synchronisation (gestion multi-démarches, réactivité des filtres) et la correction de bugs critiques liés à la perte de données. L'expérience utilisateur a été améliorée via un système d'aide plus flexible, tandis que l'infrastructure de développement a été optimisée.

### Évolutions fonctionnelles
- Support de la synchronisation automatique pour plusieurs démarches simultanées [#491](https://github.com/betagouv/OTP-DS-to-Grist/issues/491).
- Amélioration du système d'aide grâce à la gestion dynamique des liens via variables d'environnement [#487](https://github.com/betagouv/OTP-DS-to-Grist/issues/487).
- Correction d'un problème de perte de données sur les champs de type "carte" [#497](https://github.com/betagouv/OTP-DS-to-Grist/issues/497).
- Optimisation de la synchronisation : déclenchement forcé lors du changement de filtres pour garantir la cohérence des données [#488](https://github.com/betagouv/OTP-DS-to-Grist/issues/488).
- Correction de l'affichage du bandeau de statut de synchronisation [#512](https://github.com/betagouv/OTP-DS-to-Grist/issues/512).
- Mise à jour des agents d'intelligence artificielle.

### Évolutions techniques
- Optimisation de la synchronisation automatique par la suppression de routes obsolètes et le renforcement de la couverture de tests [#478](https://github.com/betagouv/OTP-DS-to-Grist/issues/478).
- Maintenance de l'infrastructure : nettoyage de la configuration Docker et correction de l'environnement Codespaces [#509](https://github.com/betagouv/OTP-DS-to-Grist/issues/509).

### Autres changements
- Mise à jour de la documentation (README).
- Évolution des agents Opencode (correction du README et gestion des sous-agents) [#501](https://github.com/betagouv/OTP-DS-to-Grist/issues/501).
- Maintenance du module DN [#515](https://github.com/betagouv/OTP-DS-to-Grist/issues/515).
