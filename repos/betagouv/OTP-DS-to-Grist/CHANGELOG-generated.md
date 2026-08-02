## Changelog : OTP-DS-to-Grist (30 derniers jours, au 01 septembre 2026)

### Résumé
Ce changelog résume les améliorations apportées à OTP-DS-to-Grist au cours du dernier mois. Les principales évolutions concernent l'amélioration de la synchronisation des données, notamment la gestion des dossiers supprimés et la synchronisation multi-dossiers, ainsi que des corrections de bugs et des améliorations de l'interface utilisateur. Des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- Ajout de la colonne `correction_instructeur` à la table `dossiers` pour suivre les corrections par les instructeurs. [#426](https://github.com/betagouv/OTP-DS-to-Grist/issues/426)
- Amélioration de la détection des dossiers supprimés via l'API DN. [#397](https://github.com/betagouv/OTP-DS-to-Grist/issues/397)
- Possibilité de synchroniser plusieurs configurations simultanément. [#434](https://github.com/betagouv/OTP-DS-to-Grist/issues/434)
- Affichage du statut de synchronisation même en l'absence de configuration.
- Ajout d'une nouvelle section "DN" pour la gestion des démarches numériques. [#394](https://github.com/betagouv/OTP-DS-to-Grist/issues/394)
- Affichage d'une bannière de statut de synchronisation pour les démarches multiples. [#403](https://github.com/betagouv/OTP-DS-to-Grist/issues/403)
- Ajout de la date de dernière correction en attente. [#411](https://github.com/betagouv/OTP-DS-to-Grist/issues/411)
- Correction de l'URL d'aide OTP. [#410](https://github.com/betagouv/OTP-DS-to-Grist/issues/410)
- Ajout de tests pour les websockets. [#449](https://github.com/betagouv/OTP-DS-to-Grist/issues/449)
- Possibilité de déclencher des vérifications et d'être réactif. [#439](https://github.com/betagouv/OTP-DS-to-Grist/issues/439)
- Amélioration des liens d'aide pour la synchronisation. [#423](https://github.com/betagouv/OTP-DS-to-Grist/issues/423)

### Évolutions techniques
- Suppression du processus `process_demarche_for_grist` remplacé par une version optimisée. [#432](https://github.com/betagouv/OTP-DS-to-Grist/issues/432)
- Masquage automatique des colonnes `_id` dans Grist. [#386](https://github.com/betagouv/OTP-DS-to-Grist/issues/386)
- Correction d'un blocage du formulaire de configuration en cas de renseignement du DN et rechargement. [#388](https://github.com/betagouv/OTP-DS-to-Grist/issues/388)
- Exécution des tâches démarches sans dossier modifié. [#430](https://github.com/betagouv/OTP-DS-to-Grist/issues/430)

### Autres changements
- Mise à jour de plusieurs dépendances (Flask, Werkzeug, Python-dotenv, Idna, etc.).
- Mise à jour des dépendances de développement (ESLint, jsdom, Vitest, etc.) pour le front-end.
- Correction de dépendances npm. [#440](https://github.com/betagouv/OTP-DS-to-Grist/issues/440)
- Revert d'une mise à jour de Flask. [#447](https://github.com/betagouv/OTP-DS-to-Grist/issues/447)
