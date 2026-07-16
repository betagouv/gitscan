## Changelog : trackdechets (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité avec l'implémentation de l'authentification multi-facteurs (MFA) et la gestion de la récupération de compte. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant la gestion des bordereaux et des informations de contact.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):**
    - Ajout de la possibilité d'activer la double authentification. [#4827](https://github.com/MTES-MCT/trackdechets/issues/4827)
    - Implémentation de la récupération de compte via un code de récupération. [#4830](https://github.com/MTES-MCT/trackdechets/issues/4830)
    - Ajout d'un panneau d'administration pour la gestion des réinitialisations MFA. [#4804](https://github.com/MTES-MCT/trackdechets/issues/4804)
    - Journalisation des événements MFA dans la base de données. [#4810](https://github.com/MTES-MCT/trackdechets/issues/4810)
- **Bordereaux:**
    - Ajout de la gestion du conditionnement (nombre, type, volume) pour les bordereaux exhaustifs. [#4825](https://github.com/MTES-MCT/trackdechets/issues/4825)
    - Correction d'un bug empêchant l'enregistrement des bordereaux de regroupement BSFF. [#4808](https://github.com/MTES-MCT/trackdechets/issues/4808)
- **Informations de contact:**
    - Correction d'un bug bloquant la modification des informations de contact du destinataire après signature de l'émetteur. [#4829](https://github.com/MTES-MCT/trackdechets/issues/4829)
    - Correction d'un problème de blocage de la signature du transporteur si les informations de contact étaient absentes. [#4813](https://github.com/MTES-MCT/trackdechets/issues/4813) et [#4794](https://github.com/MTES-MCT/trackdechets/issues/4794)
- **Mentions Légales:**
    - Intégration des mentions légales et de la politique de confidentialité en page web (au lieu de PDF). [#4833](https://github.com/MTES-MCT/trackdechets/issues/4833)
- **Unités de mesure:**
    - Correction de l'affichage des quantités en kg au lieu de tonnes dans l'aperçu et le formulaire BSFF. [#4800](https://github.com/MTES-MCT/trackdechets/issues/4800)

### Évolutions techniques
- Suppression de Crisp des cookies pour améliorer la confidentialité. [#4822](https://github.com/MTES-MCT/trackdechets/issues/4822)
- Refactoring du code pour réduire la complexité cognitive dans la gestion de l'authentification à deux facteurs.
- Correction de problèmes de linting et de formatage du code.
- Amélioration de la gestion des migrations de la base de données.

### Autres changements
- Ajout d'un changelog. [#4805](https://github.com/MTES-MCT/trackdechets/issues/4805)
- Correction de messages d'erreur et amélioration de la formulation (wording) pour l'authentification multi-facteurs.
- Assouplissement du contrôle de format du numéro Gistrid pour les BSDD. [#4796](https://github.com/MTES-MCT/trackdechets/issues/4796) et [#4797](https://github.com/MTES-MCT/trackdechets/issues/4797)
- Correction de problèmes liés aux tests d'intégration et aux pipelines CI/CD.
