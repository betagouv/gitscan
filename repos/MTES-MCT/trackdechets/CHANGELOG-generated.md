## Changelog : trackdechets (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité avec l'implémentation de l'authentification multi-facteurs (MFA) et la gestion des réinitialisations de compte. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant la gestion des bordereaux de déchets et des informations de contact.

### Évolutions fonctionnelles
- Ajout de la gestion des réinitialisations MFA via un panneau d'administration. [#4804](https://github.com/MTES-MCT/trackdechets/issues/4804)
- Implémentation de la récupération de compte via un code de récupération dans le cadre de l'authentification multi-facteurs. [#4830](https://github.com/MTES-MCT/trackdechets/issues/4830)
- Activation de la double authentification (MFA) avec révisions des codes. [#4827](https://github.com/MTES-MCT/trackdechets/issues/4827)
- Ajout de la conditionnalité d'affichage des éléments MFA et Crisp en fonction de l'environnement (Sandbox, Production). [#4835](https://github.com/MTES-MCT/trackdechets/issues/4835)
- Ajout des champs "Conditionnement" (Nombre, Type, Volume) pour les bordereaux de déchets. [#4825](https://github.com/MTES-MCT/trackdechets/issues/4825)
- Intégration des mentions légales et de la politique de confidentialité en page web (au lieu de PDF). [#4833](https://github.com/MTES-MCT/trackdechets/issues/4833)
- Amélioration de la gestion des informations de contact du destinataire après signature de l'émetteur.
- Correction d'un blocage de la signature du transporteur si les informations de contact étaient absentes. [#4813](https://github.com/MTES-MCT/trackdechets/issues/4813)
- Correction d'un blocage de modification des informations de contact du destinataire. [#4829](https://github.com/MTES-MCT/trackdechets/issues/4829)
- Correction d'un problème empêchant l'enregistrement d'un bordereau de regroupement BSFF. [#4808](https://github.com/MTES-MCT/trackdechets/issues/4808)
- Correction de l'affichage de la quantité en kg au lieu de tonnes dans l'aperçu et le formulaire BSFF. [#4800](https://github.com/MTES-MCT/trackdechets/issues/4800)

### Évolutions techniques
- Journalisation des événements MFA dans la base de données. [#4810](https://github.com/MTES-MCT/trackdechets/issues/4810)
- Refactoring et changement du type de la quantité de `Int` à `String` pour améliorer la flexibilité.
- Suppression de Crisp des cookies pour améliorer la conformité. [#4822](https://github.com/MTES-MCT/trackdechets/issues/4822)
- Ajout d'un changelog. [#4836](https://github.com/MTES-MCT/trackdechets/issues/4836)
- Amélioration de la gestion des tests d'intégration et correction de problèmes liés à ceux-ci.
- Réduction de la complexité cognitive du code.
- Correction de problèmes de pipelines et de tests.

### Autres changements
- Correction de divers messages d'erreur.
- Amélioration de la documentation et de la configuration.
- Correction de problèmes de formatage et de linting.
- Correction de problèmes liés aux migrations de la base de données.
- Assouplissement du contrôle de format sur le champ `gistridNumber` pour les BSDD. [#4796](https://github.com/MTES-MCT/trackdechets/issues/4796) et [#4797](https://github.com/MTES-MCT/trackdechets/issues/4797)
- Ajout de notifications de sécurité liées à la récupération manuelle du compte. [#4805](https://github.com/MTES-MCT/trackdechets/issues/4805)
