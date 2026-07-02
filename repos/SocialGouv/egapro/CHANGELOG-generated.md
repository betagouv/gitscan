## Changelog : egapro (30 derniers jours, au 01 Juillet 2026)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière d'accessibilité et de conformité. Des correctifs ont été apportés pour améliorer la navigation, la clarté des informations et la fidélité visuelle avec les maquettes Figma. Des améliorations techniques ont également été apportées pour l'analyse des données et l'automatisation des tests.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité : correction du contraste du tag "élevé" et des encarts d'avertissement [#3720](https://github.com/SocialGouv/egapro/issues/3720) [#3758](https://github.com/SocialGouv/egapro/issues/3758).
- Amélioration de la navigation : lecture seule de la déclaration navigable après la date limite de modification [#3716](https://github.com/SocialGouv/egapro/issues/3716) [#3798](https://github.com/SocialGouv/egapro/issues/3798).
- Amélioration du parcours de conformité : lecture seule du parcours de conformité [#3494](https://github.com/SocialGouv/egapro/issues/3494) [#3755](https://github.com/SocialGouv/egapro/issues/3755).
- Amélioration de l'interface : repositionnement des indicateurs par catégories, date au format Medium et libellé de catégorie corrigés [#3721](https://github.com/SocialGouv/egapro/issues/3721) [#3779](https://github.com/SocialGouv/egapro/issues/3779).
- Amélioration de l'interface : bouton "Mettre à jour l'existence d'un CSE" transformé en bouton secondaire [#3722](https://github.com/SocialGouv/egapro/issues/3722) [#3781](https://github.com/SocialGouv/egapro/issues/3781).
- Ajout de l'historique des statuts dans l'application [#3584](https://github.com/SocialGouv/egapro/issues/3584) [#3611](https://github.com/SocialGouv/egapro/issues/3611).
- Amélioration de l'affichage du récapitulatif de la deuxième déclaration [#3650](https://github.com/SocialGouv/egapro/issues/3650).
- Amélioration de l'affichage de la bannière d'entreprise [#3532](https://github.com/SocialGouv/egapro/issues/3532) [#3573](https://github.com/SocialGouv/egapro/issues/3573).
- Préservation de l'URL cible lors de la redirection après la connexion [#3718](https://github.com/SocialGouv/egapro/issues/3718).

### Évolutions techniques
- Refactorisation du contexte de verrouillage pour unifier l'impersonation et le verrou collaboratif [#3794](https://github.com/SocialGouv/egapro/issues/3794).
- Ajout d'un agent e2e-dev en fin de pipeline pour des tests de bout en bout [#3654](https://github.com/SocialGouv/egapro/issues/3654).
- Ajout d'un check de journal monotone pour éviter l'omission silencieuse des migrations [#3557](https://github.com/SocialGouv/egapro/issues/3557) [#3560](https://github.com/SocialGouv/egapro/issues/3560).
- Ajout d'un seed pour les données Matomo en local pour les tests [#3787](https://github.com/SocialGouv/egapro/issues/3787).
- Ajout de statistiques sur l'engagement des CSE et le nombre d'utilisateurs par entreprise [#3756](https://github.com/SocialGouv/egapro/issues/3756).
- Implémentation du plan de tracking Matomo (événements client et documentation) [#3625](https://github.com/SocialGouv/egapro/issues/3625).
- Mise en place d'un lock pour le parcours utilisateur [#3556](https://github.com/SocialGouv/egapro/issues/3556) [#3753](https://github.com/SocialGouv/egapro/issues/3753).
- Ajout d'un agent tu-dev pour l'écriture de tests unitaires et d'intégration [#3620](https://github.com/SocialGouv/egapro/issues/3620).
- Correction de l'installation de Playwright pour éviter les blocages [#3591](https://github.com/SocialGouv/egapro/issues/3591).
- Amélioration de la conformité CNIL avec Matomo (exemption de consentement) [#3655](https://github.com/SocialGouv/egapro/issues/3655).
- Ajout de graphes Matomo dans l'espace administrateur [#3658](https://github.com/SocialGouv/egapro/issues/3658).
- Ajout d'événements Matomo pour l'indicateur 7 et les liens d'aide [#3707](https://github.com/SocialGouv/egapro/issues/3707).
- Amélioration des URLs et refactorisation du système de templates pour les notifications [#3606](https://github.com/SocialGouv/egapro/issues/3606).
- Ajout d'un gate de fidélité visuelle avec design-validator (Figma ↔ rendu) [#3749](https://github.com/SocialGouv/egapro/issues/3749).

### Autres changements
- Ajout d'un diagramme de flux du parcours CSE 2027 avec superposition des étapes FSM [#3433](https://github.com/SocialGouv/egapro/issues/3433).
- Suppression des tests e2e lors de la fusion des fonctionnalités épiques [#3635](https://github.com/SocialGouv/egapro/issues/3635).
- Ajout de scripts pour le seed de données de statistiques en local [#3569](https://github.com/SocialGouv/egapro/issues/3569).
- Documentation mise à jour.
