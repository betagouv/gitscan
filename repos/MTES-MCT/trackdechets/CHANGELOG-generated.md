## Changelog : trackdechets (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité avec l'implémentation de l'authentification multi-facteurs (MFA), la correction de plusieurs blocages et bugs impactant l'utilisation des bordereaux (BSFF, BSDA, VHU) et l'amélioration de l'expérience utilisateur, notamment en permettant une saisie plus flexible des numéros de conteneurs et en ajoutant des fonctionnalités de récupération de compte.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):**
    - Ajout de logs pour les événements MFA en base de données [#4810](https://github.com/MTES-MCT/trackdechets/issues/4810).
    - Implémentation d'un panneau d'administration pour la gestion des réinitialisations MFA [#4804](https://github.com/MTES-MCT/trackdechets/issues/4804) et [#4793](https://github.com/MTES-MCT/trackdechets/issues/4793).
    - Ajout d'une fonctionnalité de récupération de compte via un code de récupération [#4799](https://github.com/MTES-MCT/trackdechets/issues/4799).
    - Notifications de sécurité liées à la récupération manuelle du compte [#4805](https://github.com/MTES-MCT/trackdechets/issues/4805).
- **Bordereaux (BSFF, BSDA, VHU):**
    - Correction d'un blocage lors de la modification du transporteur sur les bordereaux VHU et BSDA si la date de prise en charge était enregistrée mais la signature échouée [#4794](https://github.com/MTES-MCT/trackdechets/issues/4794).
    - Correction d'un blocage lors de la signature du transporteur sur les BSDD si les informations de contact étaient absentes [#4795](https://github.com/MTES-MCT/trackdechets/issues/4795).
    - Correction d'un problème empêchant l'enregistrement d'un bordereau de regroupement BSFF [#4808](https://github.com/MTES-MCT/trackdechets/issues/4808).
- **Saisie de données:**
    - Assouplissement du contrôle de format sur le `gistridNumber` (numéro Gistrid) pour les déclarations au registre national [#4797](https://github.com/MTES-MCT/trackdechets/issues/4797) et les BSDD [#4796](https://github.com/MTES-MCT/trackdechets/issues/4796).
    - Possibilité de saisir des caractères spéciaux dans le numéro de conteneur [#4786](https://github.com/MTES-MCT/trackdechets/issues/4786).
- **Autres:**
    - Correction du retour de la recette aperçu [#4785](https://github.com/MTES-MCT/trackdechets/issues/4785).
    - Correction des labels Réelle & Estimée pour PAOH & VHU [#4783](https://github.com/MTES-MCT/trackdechets/issues/4783).
    - Ajout de l'onglet détenteur et des champs manquants [#4784](https://github.com/MTES-MCT/trackdechets/issues/4784).

### Évolutions techniques
- Refactorisation du composant `SecondFactor` pour une meilleure clarté.
- Réduction de la complexité cognitive dans la classe `SecondFactor`.
- Correction de problèmes de pipelines et de tests d'intégration liés à l'implémentation de MFA.
- Correction de problèmes de migrations.

### Autres changements
- Mise à jour du bandeau et du changelog pour la recette de mai 2026 [#4789](https://github.com/MTES-MCT/trackdechets/issues/4789).
- Corrections de linting et de formatage du code.
- Suppression de code de développement lié à MFA.
