## Changelog : csplab (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'ingestion de données, notamment avec l'ajout de la gestion des webhooks TalentSoft et l'archivage des offres. L'interface utilisateur a également été améliorée, avec l'ajout de pages statiques (mentions légales, confidentialité, accessibilité, conditions d'utilisation) et l'implémentation de tests E2E pour le parcours CV. Des optimisations et des corrections de bugs ont été apportées à divers composants du système.

### Évolutions fonctionnelles
- Ajout de pages statiques : mentions légales, politique de confidentialité, accessibilité et conditions d'utilisation. [#224](https://github.com/betagouv/csplab/issues/224), [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226), [#227](https://github.com/betagouv/csplab/issues/227)
- Possibilité d'afficher l'organisation ou le ministère associé à une offre d'emploi dans les cartes et les tiroirs d'opportunités. [#443](https://github.com/betagouv/csplab/issues/443)
- Ajout d'un filtre de catégorie incluant A+. [#482](https://github.com/betagouv/csplab/issues/482)
- Implémentation de tests E2E pour le parcours CV, améliorant la qualité et la fiabilité de l'interface utilisateur. [#460](https://github.com/betagouv/csplab/issues/460), [#461](https://github.com/betagouv/csplab/issues/461), [#463](https://github.com/betagouv/csplab/issues/463)
- Ajout d'un usecase pour récupérer le détail d'une opportunité avec les métiers associés. [#487](https://github.com/betagouv/csplab/issues/487)
- Gestion des webhooks TalentSoft pour l'archivage des offres. [#512](https://github.com/betagouv/csplab/issues/512)
- Ajout d'un endpoint API pour lister les offres. [#440](https://github.com/betagouv/csplab/issues/440)

### Évolutions techniques
- Refonte de l'architecture d'ingestion avec la création d'une nouvelle application. [#493](https://github.com/betagouv/csplab/issues/493)
- Amélioration de la robustesse du mapping des ministères dans l'ingestion. [#548](https://github.com/betagouv/csplab/issues/548)
- Renommage de colonnes pour le ConcoursCleaner. [#511](https://github.com/betagouv/csplab/issues/511)
- Refactorisation de l'OfferFactory. [#514](https://github.com/betagouv/csplab/issues/514)
- Renommage de `tycho` en `web`. [#515](https://github.com/betagouv/csplab/issues/515)
- Mise à jour de la documentation OpenAPI. [#546](https://github.com/betagouv/csplab/issues/546)
- Suppression de la dépendance pgvector. [#386](https://github.com/betagouv/csplab/issues/386)
- Amélioration de la gestion des erreurs dans l'ingestion pour éviter l'arrêt du processus. [#509](https://github.com/betagouv/csplab/issues/509)
- Prévention de l'inspection dynamique de la base de données lors de la génération de la documentation de l'API. [#504](https://github.com/betagouv/csplab/issues/504)
- Mise à jour des dépendances (notebook, ocr, tycho). [#497](https://github.com/betagouv/csplab/issues/497), [#496](https://github.com/betagouv/csplab/issues/496), [#495](https://github.com/betagouv/csplab/issues/495)
- Ajout de tests de couverture et parallélisation des tests E2E. [#494](https://github.com/betagouv/csplab/issues/494)
- Remplacement des configurations Pydantic dépréciées par SettingsConfigDict. [#489](https://github.com/betagouv/csplab/issues/489)
- Amélioration de la configuration pour l'environnement de développement (désactivation des validateurs de mot de passe). [#448](https://github.com/betagouv/csplab/issues/448)

### Autres changements
- Documentation de l'installation des hooks Git. [#472](https://github.com/betagouv/csplab/issues/472)
- Documentation des webhooks TalentSoft. [#503](https://github.com/betagouv/csplab/issues/503)
- Mise à jour de la documentation sur les commandes de chargement. [#481](https://github.com/betagouv/csplab/issues/481)
- Ajout de tests pour l'interface utilisateur et refactorisation des fixtures et des factories. [#467](https://github.com/betagouv/csplab/issues/467)
- Correction de la version de Python dans l'ingestion. [#501](https://github.com/betagouv/csplab/issues/501)
- Mise à jour du CHANGELOG pour les versions 0.1.7 et 0.1.8. [#418](https://github.com/betagouv/csplab/issues/418), [#375](https://github.com/betagouv/csplab/issues/375)
- Ajout de la possibilité de nettoyer les métiers. [#451](https://github.com/betagouv/csplab/issues/451), [#398](https://github.com/betagouv/csplab/issues/398)
- Amélioration du logging avec l'utilisation d'interpolation de chaînes paresseuses. [#412](https://github.com/betagouv/csplab/issues/412)
- Correction d'un bug empêchant le bootstrap de fonctionner sur une installation propre. [#399](https://github.com/betagouv/csplab/issues/399)
- Correction d'un problème de navigation clavier dans les tests E2E. [#463](https://github.com/betagouv/csplab/issues/463)
- Correction d'un bug lié à l'affichage des filtres actifs sur la page de chargement. [#380](https://github.com/betagouv/csplab/issues/380)
- Correction d'un problème de lecture des caractères '+' non encodés dans les signatures. [#506](https://github.com/betagouv/csplab/issues/506)
- Mise à jour de la taille de la clé de chiffrement. [#474](https://github.com/betagouv/csplab/issues/474)
