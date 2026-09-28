## Changelog : device-management (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois a été marqué par une montée en maturité de la gestion des versions et de la communication avec les extensions. Le système permet désormais de définir une version de référence pour chaque plugin et d'envoyer des messages ciblés (annonces, sondages) aux utilisateurs. L'intégration avec LibreOffice a été grandement simplifiée, et de nouveaux outils de suivi de l'utilisation du parc (en version bêta) ont été introduits pour améliorer la supervision.

### Évolutions fonctionnelles
- **Gestion des versions par plugin** : Introduction d'une "version générale" pour chaque extension. L'administrateur peut désormais choisir quelle version est distribuée par défaut à l'ensemble des utilisateurs via l'interface d'administration [#40](https://github.com/IA-Generative/device-management/pull/40).
- **Intégration native LibreOffice** : Mise en place d'un flux de catalogue dédié permettant à LibreOffice de détecter et de gérer les mises à jour de manière native [#4](https://github.com/IA-Generative/device-management/pull/4).
- **Système de communications** : Déploiement d'un module permettant d'envoyer des annonces, alertes ou sondages aux extensions. Ces messages peuvent être ciblés par cohorte ou par version, et les clients peuvent désormais en accuser réception [#39](https://github.com/IA-Generative/device-management/pull/39).
- **Suivi du parc (Bêta)** : Ajout de fonctionnalités d'exportation des données d'usage (agrégats et deltas) pour permettre une analyse plus fine de l'utilisation des extensions.
- **Administration** : Amélioration de la fiche plugin permettant de renseigner directement l'identifiant spécifique à LibreOffice et ajout d'une section de débogage pour l'export manuel des données de suivi.

### Évolutions techniques
- **Auto-documentation de l'image** : L'image Docker porte désormais son propre journal de bord. L'historique des versions est intégré et consultable via l'endpoint `/__version__`.
- **Sécurité et intégrité des fichiers** :
    - Correction d'un problème de cache : les binaires sont désormais systématiquement vérifiés via leur checksum avant d'être servis [#5](https://github.com/IA-Generative/device-management/pull/5).
    - Renforcement de la sécurité des sessions d'administration (retrait des tokens sensibles des cookies).
    - Sécurisation de la génération des flux XML (échappement des attributs) pour prévenir les vulnérabilités.
- **Optimisation du catalogue** : Refactorisation du moteur de versioning pour utiliser un parseur unique et optimisation des requêtes de disponibilité des versions via PostgreSQL.
- **Déploiement** : Automatisation de la déclaration de la version dans les images déployées pour éviter les décalages entre le code et l'image.

### Autres changements
- **Documentation** : Mise à jour majeure de la documentation destinée aux développeurs d'extensions (contrats de communication, sémantique des flux LibreOffice et gestion des versions).
- **Tests** : Renforcement significatif de la couverture de tests, notamment sur les flux de mise à jour, la gestion des versions et les nouveaux contrats d'export de données.
