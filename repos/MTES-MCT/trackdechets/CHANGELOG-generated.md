## Changelog : trackdechets (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité avec l'implémentation de l'authentification multi-facteurs (MFA) et la gestion des réinitialisations de mot de passe. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant la saisie de données et la gestion des bordereaux.

### Évolutions fonctionnelles
- **Authentification Multi-Facteurs (MFA):**
    - Ajout de la journalisation des événements MFA dans la base de données [#4810](https://github.com/MTES-MCT/trackdechets/issues/4810).
    - Mise en place d'un panneau d'administration pour gérer les réinitialisations MFA [#4804](https://github.com/MTES-MCT/trackdechets/issues/4804) et [#4799](https://github.com/MTES-MCT/trackdechets/issues/4799).
    - Possibilité de récupérer son compte via un code de récupération [#4799](https://github.com/MTES-MCT/trackdechets/issues/4799).
- **Gestion des bordereaux:**
    - Correction d'un blocage lors de la modification du transporteur sur les VHU et BSDA si la date de prise en charge était enregistrée mais la signature échouée [#4794](https://github.com/MTES-MCT/trackdechets/issues/4794).
    - Correction d'un blocage de la signature du transporteur sur les BSDD si les informations de contact étaient manquantes [#4795](https://github.com/MTES-MCT/trackdechets/issues/4795).
    - Résolution d'un problème empêchant l'enregistrement d'un bordereau de regroupement BSFF [#4808](https://github.com/MTES-MCT/trackdechets/issues/4808) et [#4788](https://github.com/MTES-MCT/trackdechets/issues/4788).
- **Améliorations diverses:**
    - Assouplissement du contrôle de format du numéro GISTRID pour les déclarations au registre national et les BSDD [#4797](https://github.com/MTES-MCT/trackdechets/issues/4797) et [#4796](https://github.com/MTES-MCT/trackdechets/issues/4796).
    - Possibilité de saisir des caractères spéciaux dans le numéro de contenant [#4786](https://github.com/MTES-MCT/trackdechets/issues/4786).
    - Correction du retour de l'aperçu recette [#4785](https://github.com/MTES-MCT/trackdechets/issues/4785).
    - Correction de l'association de l'onglet BSFF avec le tableau des conteneurs [#4788](https://github.com/MTES-MCT/trackdechets/issues/4788).

### Évolutions techniques
- **Sécurité:**
    - Ajout de notifications de sécurité liées à la récupération manuelle du compte [#4805](https://github.com/MTES-MCT/trackdechets/issues/4805).
- **Refactoring:**
    - Refactorisation du composant SecondFactor pour une meilleure clarté.
- **Tests:**
    - Ajout de tests d'intégration pour l'authentification multi-facteurs.
    - Correction de problèmes dans les pipelines de tests.

### Autres changements
- Mise à jour du changelog et du bandeau d'information MEP pour juin 2026 [#4789](https://github.com/MTES-MCT/trackdechets/issues/4789).
- Corrections de problèmes de linting dans le code.
- Correction d'un problème de migration dupliquée.
- Correction d'un problème de complexité cognitive dans le code.
