## Changelog : OTP-DS-to-Grist (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante en renforçant la sécurité des accès et en automatisant davantage de tâches grâce à l'introduction de nouveaux agents intelligents. La synchronisation des données est devenue plus rapide, plus fiable et plus transparente pour l'utilisateur final.

### Évolutions fonctionnelles
- **Automatisation :** Introduction de nouveaux agents (Opencode) pour la gestion des logs, du reviewer, de Grist et de DN.
- **Nouvelle fonctionnalité :** Ajout de la sauvegarde automatique multiple ([#514](https://github.com/betagouv/OTP-DS-to-Grist/issues/514)).
- **Corrections d'interface et d'usage :**
  - Correction de l'OCR pour les colonnes de pièces jointes ([#558](https://github.com/betagouv/OTP-DS-to-Grist/issues/558)).
  - Résolution de problèmes de lecture de données Grist ([#555](https://github.com/betagouv/OTP-DS-to-Grist/issues/555)).
  - Correction de l'affichage du bandeau de synchronisation ([#512](https://github.com/betagouv/OTP-DS-to-Grist/issues/512)).
  - Forçage de la synchronisation lors du changement de filtre ([#488](https://github.com/betagouv/OTP-DS-to-Grist/issues/488)).

### Évolutions techniques
- **Sécurité :** 
  - Renforcement de l'authentification via l'utilisation obligatoire des tokens Grist ([#562](https://github.com/betagouv/OTP-DS-to-Grist/issues/562), [#566](https://github.com/betagouv/OTP-DS-to-Grist/issues/566)).
  - Restriction des URLs Grist autorisées ([#551](https://github.com/betagouv/OTP-DS-to-Grist/issues/551)) et mise en place de Fail2Ban ([#547](https://github.com/betagouv/OTP-DS-to-Grist/issues/547)).
  - Amélioration de la vérification des accès ([#574](https://github.com/betagouv/OTP-DS-to-Grist/issues/574)).
- **Optimisation de la synchronisation :**
  - Récupération des dossiers par lots pour plus d'efficacité ([#536](https://github.com/betagouv/OTP-DS-to-Grist/issues/536)).
  - Ajout de l'auto-séquence de synchronisation ([#587](https://github.com/betagouv/OTP-DS-to-Grist/issues/587)) et stockage de la durée des synchronisations en base de données ([#581](https://github.com/betagouv/OTP-DS-to-Grist/issues/581)).
  - Correction de la gestion des clés pour les lignes répétables ([#549](https://github.com/betagouv/OTP-DS-to-Grist/issues/549)).
- **Performance et Cache :**
  - Accélération des filtres serveur DN ([#561](https://github.com/betagouv/OTP-DS-to-Grist/issues/561)).
  - Optimisation de la gestion du cache pour les blocs répétables ([#504](https://github.com/betagouv/OTP-DS-to-Grist/issues/504)) et pour les données Grist ([#554](https://github.com/betagouv/OTP-DS-to-Grist/issues/554)).
- **Refactoring :**
  - Isolation de la classe de gestion des limites de débit (`rate_limited_session`) ([#534](https://github.com/betagouv/OTP-DS-to-Grist/issues/534)).
  - Réorganisation des tâches de vérification des dossiers supprimés ([#580](https://github.com/betagouv/OTP-DS-to-Grist/issues/580)).

### Autres changements
- **Nettoyage :** Suppression de code mort concernant les blocs répétables et le client Grist ([#578](https://github.com/betagouv/OTP-DS-to-Grist/issues/578)).
- **Configuration :** Correction d'un bug empêchant la conservation du token DN si la clé Grist est manquante ([#584](https://github.com/betagouv/OTP-DS-to-Grist/issues/584)).
- **Maintenance :** Correction des chemins pour les polices de caractères DSFR.
