## Changelog : Archives-Mail-Thunderbird-Distribution (30 derniers jours, au 28 juin 2026)

### Résumé
Cette mise à jour majeure se concentre sur l'amélioration de la documentation et l'ajout de fonctionnalités pour faciliter l'archivage automatisé des emails avec les versions récentes de Thunderbird (140+). L'outil est désormais mieux adapté aux environnements utilisant Thunderbird ESR moderne et propose une nouvelle option d'archivage automatisé basée sur un module complémentaire.

### Évolutions fonctionnelles
- Ajout d'une option d'archivage automatisé pour Thunderbird ESR moderne, utilisant un module complémentaire. [#2026-06-28T14:20:31+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/0a9804e)
- Amélioration du mode opératoire pour Thunderbird 140+ avec une navigation détaillée de l'interface et des instructions claires pour l'archivage. [#2026-06-28T14:54:19+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/0256e69)
- Documentation détaillée des quatre options disponibles dans le module AutoarchiveReloaded. [#2026-06-28T14:52:23+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/54d4c54)
- Ajout d'un script `aide-dates-archivage.bat` pour calculer les dates butoirs d'archivage (3, 6, 12 mois). [#2026-06-28T14:20:31+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/daccd4f)
- Mise à jour de la documentation pour prendre en compte les versions antérieures de Thunderbird sans l'option "Ancienneté en jours", en utilisant un critère basé sur la date. [#2026-06-28T14:16:40+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/88cd0a1)
- Simplification du démarrage rapide et ajout d'une section "Tests à mener (recette)" dans le README. [#2026-06-28T13:44:10+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/b49bd5f)

### Évolutions techniques
- Restructuration de la documentation pour une meilleure orientation vers Thunderbird 140+, avec l'utilisation de schémas Mermaid. [#2026-06-28T14:44:20+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/7a93df8)
- Durcissement de la sécurité du dépôt avec un `.gitignore` plus restrictif, un dossier `private/` et l'intégration de `gitleaks` pour prévenir les fuites d'informations sensibles. [#2026-06-28T13:24:26+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/e4ae6ca)

### Autres changements
- Mise à jour de la note de cadrage, retirant la recommandation de Dovecot. [#2026-06-28T20:43:53+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/2ee7bb4)
- Ajout d'une section dédiée à la configuration des scripts (.bat) dans la documentation. [#2026-06-28T16:03:07+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/c429bc9)
- Ajout de captures d'écran pour Thunderbird 140+ et AutoarchiveReloaded, avec anonymisation et instructions pour quitter/relancer Thunderbird. [#2026-06-28T15:29:04+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/db3604a)
- Précision sur l'impossibilité d'exécuter deux versions de Thunderbird simultanément, avec une astuce pour utiliser l'option `-no-remote` et des profils différents. [#2026-06-28T14:30:30+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/2754b53)
- Correction de l'ignorance des fichiers verrouillés Office (~$*) dans le `.gitignore`. [#2026-06-28T20:32:34+02:00](https://github.com/IA-Generative/Archives-Mail-Thunderbird-Distribution/commit/cdf3765)
