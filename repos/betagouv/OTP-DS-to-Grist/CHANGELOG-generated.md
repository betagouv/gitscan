## Changelog : OTP-DS-to-Grist (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante dans la sécurisation et l'optimisation de la synchronisation des données. Les utilisateurs bénéficieront d'une gestion plus robuste des jetons d'accès (tokens) et de nouvelles fonctionnalités de sauvegarde automatique, tandis que le système devient plus performant grâce à un traitement par lots et une meilleure gestion du cache.

### Évolutions fonctionnelles
- **Sécurité et authentification :** Support des jetons Grist pour l'authentification ([#562](https://github.com/betagouv/OTP-DS-to-Grist/issues/562), [#566](https://github.com/betagouv/OTP-DS-to-Grist/issues/566)), restriction de l'URL Grist ([#551](https://github.com/betagouv/OTP-DS-to-Grist/issues/551)) et amélioration de la vérification des accès ([#574](https://github.com/betagouv/OTP-DS-to-Grist/issues/574)).
- **Synchronisation :** Nouvelle fonction de synchronisation automatique des séquences ([#587](https://github.com/betagouv/OTP-DS-to-Grist/issues/587)), mise en place de la sauvegarde automatique multiple ([#514](https://github.com/betagouv/OTP-DS-to-Grist/issues/514)) et suppression automatique des lignes de blocs supprimés dans Grist ([#582](https://github.com/betagouv/OTP-DS-to-Grist/issues/582)).
- **Corrections :** Résolution de problèmes liés à l'OCR sous les colonnes de pièces jointes ([#558](https://github.com/betagouv/OTP-DS-to-Grist/issues/558)), aux échecs de lecture Grist ([#555](https://github.com/betagouv/OTP-DS-to-Grist/issues/555)) et à la persistance de la configuration ([#584](https://github.com/betagouv/OTP-DS-to-Grist/issues/584)).

### Évolutions techniques
- **Performance :** Récupération des dossiers par lots ([#536](https://github.com/betagouv/OTP-DS-to-Grist/issues/536)), optimisation des filtres serveur pour les dossiers ([#561](https://github.com/betagouv/OTP-DS-to-Grist/issues/561)) et amélioration de la gestion du cache pour Grist et les blocs répétables ([#554](https://github.com/betagouv/OTP-DS-to-Grist/issues/554), [#504](https://github.com/betagouv/OTP-DS-to-Grist/issues/504)).
- **Architecture :** Introduction de nouveaux agents spécialisés (DN, Grist, Reviewer, Logs), refactorisation de la structure des tâches de synchronisation ([#580](https://github.com/betagouv/OTP-DS-to-Grist/issues/580)) et stockage de la durée des synchronisations en base de données ([#581](https://github.com/betagouv/OTP-DS-to-Grist/issues/581)).
- **Sécurité et infrastructure :** Mise en place de fail2ban pour la protection du service ([#547](https://github.com/betagouv/OTP-DS-to-Grist/issues/547)).
- **Qualité du code :** Normalisation des noms de colonnes ([#579](https://github.com/betagouv/OTP-DS-to-Grist/issues/579)) et isolation de la logique de gestion du rate-limiting ([#534](https://github.com/betagouv/OTP-DS-to-Grist/issues/534)).

### Autres changements
- **Nettoyage :** Suppression de code mort (blocs répétables et GristClient) ([#578](https://github.com/betagouv/OTP-DS-to-Grist/issues/578)).
- **Assets :** Correction du chemin d'accès pour les polices de caractères DSFR.
