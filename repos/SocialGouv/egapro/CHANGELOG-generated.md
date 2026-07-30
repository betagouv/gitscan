## Changelog : egapro (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment des corrections de bugs impactant la soumission des déclarations, l'affichage des données et la navigation. Des améliorations techniques ont également été apportées pour faciliter les déploiements et améliorer la robustesse de la plateforme, ainsi que des optimisations pour l'accessibilité.

### Évolutions fonctionnelles
- Ajout du numéro de version dans le footer de l'application [#4047](https://github.com/SocialGouv/egapro/issues/4047).
- Correction de l'alignement de l'alerte "Prochaines étapes" avec l'indicateur G [#4049](https://github.com/SocialGouv/egapro/issues/4049).
- Correction du dénominateur des proportions variable H/F dans la déclaration [#4048](https://github.com/SocialGouv/egapro/issues/4048).
- Documentation des écarts comme des ratios avec la bonne convention de signe dans l'API publique [#4041](https://github.com/SocialGouv/egapro/issues/4041).
- Affichage des écarts avec 2 décimales tronquées [#4039](https://github.com/SocialGouv/egapro/issues/4039).
- Rendre le seuil de 5% symétrique [#4040](https://github.com/SocialGouv/egapro/issues/4040).
- Masquage de la section CSE lorsque aucun avis n'est attendu [#4032](https://github.com/SocialGouv/egapro/issues/4032).
- Correction du parcours "justification des écarts" sans CSE [#4027](https://github.com/SocialGouv/egapro/issues/4027).
- Correction des accordéons inutilisables après suppression puis ré-import [#4025](https://github.com/SocialGouv/egapro/issues/4025).
- Correction de la deadline de la déclaration 2 en phase 2 et ré-soumission depuis l'état "en attente de choix" [#4003](https://github.com/SocialGouv/egapro/issues/4003).
- Correction de l'affichage du bandeau entreprise et du libellé d'étape de la démarche Représentation [#4024](https://github.com/SocialGouv/egapro/issues/4024).
- Correction des bordures invisibles des cases à cocher et des radios sous Firefox [#4026](https://github.com/SocialGouv/egapro/issues/4026).
- Prévention des téléchargements multiples du PDF [#4019](https://github.com/SocialGouv/egapro/issues/4019).
- Correction du panneau latéral aveugle à la taille et au flag CSE [#4000](https://github.com/SocialGouv/egapro/issues/4000).
- Correction de la position des marques combinantes dans les polices embarquées du PDF [#4018](https://github.com/SocialGouv/egapro/issues/4018).
- Blocage de la soumission du formulaire lorsque les champs de rémunération sont manquants pour un effectif non nul [#4002](https://github.com/SocialGouv/egapro/issues/4002).
- Exposition des catégories d'emplois dans l'API SUIT [#3992](https://github.com/SocialGouv/egapro/issues/3992).
- Affichage de la source des catégories d'emplois en libellé lisible dans le PDF [#4016](https://github.com/SocialGouv/egapro/issues/4016).
- Message d'erreur CSE explicite en français dans le bandeau informations manquantes [#3997](https://github.com/SocialGouv/egapro/issues/3997).
- Ajout d'un bucket "medium-150" pour couvrir la tranche d'effectif de 100 à 149 dans le mock GIP-MDS [#3991](https://github.com/SocialGouv/egapro/issues/3991).
- Suppression du code NAF et restauration du libellé de l'effectif dans le bandeau CompanyBanner [#4013](https://github.com/SocialGouv/egapro/issues/4013).
- Ajout d'un bouton "Je donne mon avis" en fin de parcours [#3966](https://github.com/SocialGouv/egapro/issues/3966).
- Implémentation du calcul des écarts signés selon les règles de conformité GIP [#3868](https://github.com/SocialGouv/egapro/issues/3868).
- Affichage de la vraie proportion de bénéficiaires [#3869](https://github.com/SocialGouv/egapro/issues/3869).
- Intégration du contenu des emails de rappel et définition des règles d'envoi [#3857](https://github.com/SocialGouv/egapro/issues/3857).
- Ajout du bouton d'export dans l'étape 5 (indicateur G) [#3968](https://github.com/SocialGouv/egapro/issues/3968).
- Lecture seule navigable après la date limite de modification [#3798](https://github.com/SocialGouv/egapro/issues/3798).

### Évolutions techniques
- La promotion bake la version dans l'image (app_version) [#4047](https://github.com/SocialGouv/egapro/issues/4047).
- Les envs de test persistants déploient une image versionnée.
- Verrouillage du compilateur du moteur d'étapes FSM [#3979](https://github.com/SocialGouv/egapro/issues/3979).
- Dérivation du vocabulaire de statut admin de DECLARATION_FSM_STATUSES [#3983](https://github.com/SocialGouv/egapro/issues/3983).
- Refonte multi-pages du template PDF [#3973](https://github.com/SocialGouv/egapro/issues/3973).
- Mise en place d'un canal prerelease alpha avec déclenchement automatique [#3858](https://github.com/SocialGouv/egapro/issues/3858).
- Migration des builds d'images de buildkit-service vers buildkit-operator [#3844](https://github.com/SocialGouv/egapro/issues/3844).
- Ajout du versioning des CGU [#2626](https://github.com/SocialGouv/egapro/issues/2626).

### Autres changements
- Changelog IA exhaustif [#4046](https://github.com/SocialGouv/egapro/issues/4046).
- Documentation du moteur d'étapes (FSM) et pointeur vers le document CLAUDE.md [#3982](https://github.com/SocialGouv/egapro/issues/3982).
- Amélioration de la nomenclature des cas de tests [#4006](https://github.com/SocialGouv/egapro/issues/4006).
- Correction du workflow de release pour les canaux alpha [#3906](https://github.com/SocialGouv/egapro/issues/3906).
- Ajout de tests unitaires et E2E pour les parcours [#3988](https://github.com/SocialGouv/egapro/issues/3988).
- Mise à jour de la documentation Figma pour assurer la cohérence visuelle [#3961](https://github.com/SocialGouv/egapro/issues/3961).
- Amélioration de l'accessibilité (RGAA) avec l'implémentation d'ultra11y [#3887](https://github.com/SocialGouv/egapro/issues/3887).
- Ajout de purge des données des déclarations [#3828](https://github.com/SocialGouv/egapro/issues/3828).
