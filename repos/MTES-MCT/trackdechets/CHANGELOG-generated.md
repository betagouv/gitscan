## Changelog : trackdechets (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité avec l'implémentation de l'authentification multi-facteurs (MFA), ainsi que sur la correction de plusieurs bugs liés à la signature des bordereaux et à la gestion des informations de contact. Des améliorations ont également été apportées à la gestion des quantités et à la configuration du système.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de récupération de compte via un code de récupération dans le cadre de l'authentification multi-facteurs (MFA) [#4830](https://github.com/MTES-MCT/trackdechets/issues/4830).
- Implémentation de l'activation de la double authentification (MFA) avec révisions des codes [#4827](https://github.com/MTES-MCT/trackdechets/issues/4827).
- Ajout d'un panneau d'administration pour la gestion des réinitialisations MFA [#4804](https://github.com/MTES-MCT/trackdechets/issues/4804).
- Ajout de la possibilité de gérer les réinitialisations MFA via un système d'alerte.
- Ajout des champs "Nombre", "Type" et "Volume" pour le conditionnement dans le registre exhaustif [#4825](https://github.com/MTES-MCT/trackdechets/issues/4825).
- Intégration des mentions légales et de la politique de confidentialité en page web (et non plus en PDF) [#4833](https://github.com/MTES-MCT/trackdechets/issues/4833).
- Possibilité d'assouplir le contrôle de format sur le numéro Gistrid (BSDD) [#4796](https://github.com/MTES-MCT/trackdechets/issues/4796) et [#4797](https://github.com/MTES-MCT/trackdechets/issues/4797).

### Évolutions techniques
- Journalisation des événements MFA dans la base de données [#4810](https://github.com/MTES-MCT/trackdechets/issues/4810).
- Refactoring du code pour réduire la complexité cognitive dans la classe SecondFactor (MFA) [#7fc3385c](https://github.com/MTES-MCT/trackdechets/commit/7fc3385c).
- Correction de problèmes de build et de SonarQube.
- Conversion des quantités affichées en kg en tonnes dans les PDF [#4800](https://github.com/MTES-MCT/trackdechets/issues/4800).
- Suppression de Crisp des cookies [#4822](https://github.com/MTES-MCT/trackdechets/issues/4822).

### Autres changements
- Correction de plusieurs bugs bloquant la signature des bordereaux (BSDD, BSDA, VHU) dans différentes situations.
- Correction d'un bug empêchant l'enregistrement d'un bordereau de regroupement BSFF.
- Correction de problèmes liés à la date de remise au collecteur sur les PDF.
- Correction de messages d'erreur Gistird BSDD.
- Amélioration de la gestion des informations de contact du destinataire.
- Ajout d'un changelog.
- Correction de problèmes de tests d'intégration et de pipelines.
- Correction de problèmes de formatage du code.
- Correction de problèmes liés aux migrations de la base de données.
