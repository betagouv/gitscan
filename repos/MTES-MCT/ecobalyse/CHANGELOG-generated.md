## Changelog : ecobalyse (30 derniers jours, au 2026-07-16)

### Résumé
Cette version apporte des améliorations significatives aux données, notamment pour les véhicules (VELI) et l'alimentation, avec l'ajout de nouveaux processus et la mise à jour des données existantes. L'interface utilisateur a également été améliorée, avec des corrections et l'ajout de fonctionnalités comme la résolution du nom complet des régions et l'accès à des commandes API authentifiées. Des optimisations techniques ont été réalisées pour améliorer la performance et la sécurité.

### Évolutions fonctionnelles
- **Explorateur:** Résolution du nom complet de la région lorsque possible. [#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658)
- **API:** Ajout de commandes API authentifiées. [#2653](https://github.com/MTES-MCT/ecobalyse/issues/2653)
- **Données (VELI):** Ajout de processus pour la modélisation selon la réglementation EV. [#2622](https://github.com/MTES-MCT/ecobalyse/issues/2622)
- **Données (VELI):** Ajout de processus intégrant le kilométrage pour la phase d'utilisation des véhicules. [#2619](https://github.com/MTES-MCT/ecobalyse/issues/2619)
- **Données (VELI):** Mise à jour des exemples de véhicules. [#2629](https://github.com/MTES-MCT/ecobalyse/issues/2629) et [#2641](https://github.com/MTES-MCT/ecobalyse/issues/2641)
- **Données (Général):** Importation de données BAFU à partir d'un export CSV Simapro. [#2626](https://github.com/MTES-MCT/ecobalyse/issues/2626)
- **Données (Alimentation):** Ajout d'un exemple de "Pizza bolognese Bio (350g)". [#2553](https://github.com/MTES-MCT/ecobalyse/issues/2553)
- **Données (Général):** Ajout de matériaux d'emballage pour les objets et les véhicules. [#2555](https://github.com/MTES-MCT/ecobalyse/issues/2555)
- **Interface Utilisateur:** Ajout d'un lien de feedback. [#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612)
- **Interface Utilisateur:** Implémentation d'étiquettes avec portée (scoped labels). [#2632](https://github.com/MTES-MCT/ecobalyse/issues/2632)
- **Interface Utilisateur:** Localisation des nouvelles transformations avec des valeurs par défaut pertinentes. [#2636](https://github.com/MTES-MCT/ecobalyse/issues/2636)

### Évolutions techniques
- **Architecture:** Activation des transports "cooled" lorsque disponibles pour la portée. [#2654](https://github.com/MTES-MCT/ecobalyse/issues/2654)
- **Tests:** Déplacement de la suite de tests E2E vers un job planifié. [#2633](https://github.com/MTES-MCT/ecobalyse/issues/2633)
- **CI/CD:** Finalisation de la fusion des dépôts de données et de front-end. [#2614](https://github.com/MTES-MCT/ecobalyse/issues/2614)
- **Sécurité:** Prévention de la falsification du jeton d'authentification. [#2600](https://github.com/MTES-MCT/ecobalyse/issues/2600)
- **Refactoring:** Refactorisation du pipeline de données pour la fusion des fichiers de processus. [#2437](https://github.com/MTES-MCT/ecobalyse/issues/2437)
- **Mises à jour:** Mise à jour des dépendances Litestar, Sentry-SDK et des dépendances de développement.
- **Elm:** Mises à jour Elm. [#2638](https://github.com/MTES-MCT/ecobalyse/issues/2638)

### Autres changements
- **Documentation:** Ajout d'une politique de sécurité. [#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608)
- **Données:** Nettoyage des ingrédients de base et des alias. [#2604](https://github.com/MTES-MCT/ecobalyse/issues/2604)
- **Données:** Renommage des activités à créer et de "Custom". [#2601](https://github.com/MTES-MCT/ecobalyse/issues/2601)
- **Données:** Ajout d'une région Maghreb. [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568)
- **Données:** Remplacement de "elecMJ" par "elecKwh". [#2561](https://github.com/MTES-MCT/ecobalyse/issues/2561)
- **Données:** Diverses mises à jour et corrections de données (sorgho, seigle, lin, haricot lima, amarante, tournesol, tomate, café, orange, etc.). [#2457](https://github.com/MTES-MCT/ecobalyse/issues/2457) à [#2514](https://github.com/MTES-MCT/ecobalyse/issues/2514) et autres.
- Correction du calcul du score total dans food1. [#2655](https://github.com/MTES-MCT/ecobalyse/issues/2655)
- Correction d'un bug empêchant le rechargement de la configuration après réception des processus détaillés. [#2627](https://github.com/MTES-MCT/ecobalyse/issues/2627)
- Suppression de processus obsolètes ou hors portée VELI. [#2472](https://github.com/MTES-MCT/ecobalyse/issues/2472)
