## Changelog : envergo (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par une restructuration majeure du module des Démarches Numériques (DN) afin d'en améliorer la fiabilité et la gestion des données. L'expérience utilisateur a été affinée grâce à une mise à jour importante des libellés, à l'amélioration de l'interface de gestion des haies et des espèces protégées, et à l'ajout de nouveaux outils de notification (récépissés automatiques). Enfin, la sécurité a été renforcée par l'implémentation d'un système de détection de bots lors des inscriptions.

### Évolutions fonctionnelles
- **Démarches Numériques (DN) :**
    - Amélioration de l'affichage des champs et des images liés aux dossiers DN sur les pages d'instruction. [#1341](https://github.com/MTES-MCT/envergo/pull/1341)
    - Automatisation de l'envoi des récépissés de DN lors de la soumission d'un dossier ou du redémarrage d'une instruction. [#1292](https://github.com/MTES-MCT/envergo/pull/1292)
    - Correction de bugs critiques provoquant des erreurs 500 lors de l'enregistrement des configurations DN. [#1314](https://github.com/MTES-MCT/envergo/pull/1314)
- **Gestion de l'environnement et des espèces :**
    - Introduction de la multicatégorisation pour les Espèces Protégées (EP).
    - Mise à jour de l'évaluateur EP avec l'intégration de nouvelles données (zones sensibles, bonus, haies).
    - Intégration de nouvelles réglementations et zones de gestion (Natura 2000, zones SI, SPR, etc.).
    - Amélioration de l'interface d'édition des haies via l'utilisation de Vue.js pour une meilleure réactivité.
- **Interface et Expérience Utilisateur (UX) :**
    - Refonte de nombreux libellés pour plus de clarté (notamment sur les notions d'urgence, d'urbanisme et de pièces d'eau). [#1349](https://github.com/MTES-MCT/envergo/pull/1349)
    - Ajout d'un bloc d'alerte "urgence" sur la page d'accueil. [#1322](https://github.com/MTES-MCT/envergo/pull/1322)
    - Amélioration de la lisibilité des informations via l'utilisation de balises d'abréviation (`<abbr>`).
    - Optimisation de la recherche de projets par référence dans l'interface d'administration.
- **Communications :**
    - Amélioration des modèles d'emails (mentions d'invitation, signatures, liens d'aide pour la rédaction manuelle).

### Évolutions techniques
- **Architecture et Refactoring :**
    - Migration complète du code lié aux Démarches Numériques vers un module dédié pour une meilleure maintenance. [#1317](https://github.com/MTES-MCT/envergo/pull/1317)
    - Refactorisation de l'architecture des pages et nettoyage important du code mort. [#1282](https://github.com/MTES-MCT/envergo/pull/1282)
    - Optimisation des performances par la mise en cache du parsing des dossiers.
- **Sécurité et Infrastructure :**
    - Implémentation d'un mécanisme de détection de bots lors de la création de compte. [#1313](https://github.com/MTES-MCT/envergo/pull/1313)
    - Stabilisation de la CI/CD par l'utilisation d'une version LTS plus ancienne d'Ubuntu. [#1346](https://github.com/MTES-MCT/envergo/pull/1346)
    - Optimisation de la gestion des fichiers volumineux par un déplacement systématique sur disque.
- **Qualité et Tests :**
    - Enrichissement et simplification de la suite de tests (E2E et unitaires).
    - Correction de divers bugs de gestion de fichiers et de fuites de ressources.

### Autres changements
- **Documentation :**
    - Mise à jour de la documentation technique sur les démarches numériques et les processus de collaboration.
    - Ajout des détails de la stack technique dans le fichier README.
- **Nettoyage :**
    - Diverses corrections de style, de commentaires et de syntaxe.
