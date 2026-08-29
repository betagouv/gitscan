## Changelog : OTP-DS-to-Grist (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'introduction de filtres multiples et d'une interface plus réactive, facilitant la gestion des données. Les capacités de suivi ont été enrichies et le moteur de synchronisation a été optimisé pour gagner en efficacité et en stabilité.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités :**
  - Introduction de filtres multiples pour affiner la sélection des données ([#459](https://github.com/betagouv/OTP-DS-to-Grist/issues/459)).
  - Ajout de la colonne `correction_instructeur` dans la table des dossiers ([#426](https://github.com/betagouv/OTP-DS-to-Grist/issues/426)).
  - Mise en place de vérifications de configuration réactives ([#439](https://github.com/betagouv/OTP-DS-to-Grist/issues/439)).
  - Exploration de la récupération des adresses e-mail des utilisateurs ([#435](https://github.com/betagouv/OTP-DS-to-Grist/issues/435)).
- **Améliorations et corrections :**
  - Optimisation du comportement des accordéons dans l'interface utilisateur ([#452](https://github.com/betagouv/OTP-DS-to-Grist/issues/452)).
  - Correction de l'affichage des blocs répétables (suppression des colonnes vides) ([#468](https://github.com/betagouv/OTP-DS-to-Grist/issues/468)).
  - Stabilisation des suffixes pour la gestion des doublons de champs ([#460](https://github.com/betagouv/OTP-DS-to-Grist/issues/460)).
  - Amélioration de la logique d'exécution des tâches pour les dossiers non modifiés ([#430](https://github.com/betagouv/OTP-DS-to-Grist/issues/430)).

### Évolutions techniques
- **Optimisation et Refactoring :**
  - Extraction de la classe `ColumnCache` pour une meilleure modularité ([#472](https://github.com/betagouv/OTP-DS-to-Grist/issues/472)).
  - Remplacement du processus de traitement des démarches par une version optimisée ([#432](https://github.com/betagouv/OTP-DS-to-Grist/issues/432)).
- **Tests :**
  - Ajout de tests pour la gestion des WebSockets ([#449](https://github.com/betagouv/OTP-DS-to-Grist/issues/449)).

### Autres changements
- Nettoyage du code mort ([#477](https://github.com/betagouv/OTP-DS-to-Grist/issues/477)).
- Mise à jour de la documentation (suppression de `technique.md`).
