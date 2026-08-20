## Changelog : egapro (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'alignement de l'interface utilisateur avec les maquettes de design (Figma), l'amélioration de la précision des calculs de l'index de rémunération et le renforcement de la fiabilité du système. La robustesse technique a été accrue grâce à une couverture de tests de bout en bout (E2E) étendue et une automatisation améliorée des processus de déploiement et de release.

### Évolutions fonctionnelles
- **Déclarations et indicateurs** :
    - Amélioration de la précision des calculs, notamment pour l'indicateur G, les écarts de rémunération et la gestion des périodes de référence ([#4111](https://github.com/SocialGouv/egapro/issues/4111), [#4121](https://github.com/SocialGouv/egapro/issues/4121), [#4048](https://github.com/SocialGouv/egapro/issues/4048)).
    - Renforcement des validations pour bloquer l'accès au tunnel si des informations essentielles (téléphone, CSE) sont manquantes ([#4117](https://github.com/SocialGouv/egapro/issues/4117)).
    - Ajout d'un bouton "Je donne mon avis" en fin de parcours ([#3966](https://github.com/SocialGouv/egapro/issues/3966)).
- **Export PDF** :
    - Refonte complète du template pour supporter le rendu multi-pages ([#3973](https://github.com/SocialGouv/egapro/issues/3973)).
    - Corrections sur l'affichage des caractères spéciaux et suppression des césures dans les en-têtes de tableaux ([#4018](https://github.com/SocialGouv/egapro/issues/4018), [#4145](https://github.com/SocialGouv/egapro/issues/4145)).
- **Expérience utilisateur (UX) et Interface (UI)** :
    - Mise en conformité globale avec les maquettes Figma : modales de profil, couleurs des liens, espacements et composants de l'espace personnel ([#4188](https://github.com/SocialGouv/egapro/issues/4188), [#4174](https://github.com/SocialGouv/egapro/issues/4174), [#4143](https://github.com/SocialGouv/egapro/issues/4143)).
    - Amélioration de la navigation, notamment la remontée automatique en haut de page lors du changement d'étape ([#4227](https://github.com/SocialGouv/egapro/issues/4227)).
    - Optimisation de l'affichage dans "Mon espace" : gestion des erreurs CSE, affichage du récapitulatif dès la soumission et masquage du bandeau archives ([#4229](https://github.com/SocialGouv/egapro/issues/4229), [#4130](https://github.com/SocialGouv/egapro/issues/4130), [#4199](https://github.com/SocialGouv/egapro/issues/4199)).
    - Corrections de bugs d'affichage, notamment sur Firefox (bordures des cases à cocher) ([#4026](https://github.com/SocialGouv/egapro/issues/4026)).

### Évolutions techniques
- **Architecture et Logique métier** :
    - Refactorisation du moteur de gestion des étapes (FSM) pour une meilleure maîtrise des transitions et des verrous d'édition ([#3979](https://github.com/SocialGouv/egapro/issues/3979), [#4120](https://github.com/SocialGouv/egapro/issues/4120)).
    - Amélioration de la cohérence des données entre les imports GIP et les effectifs affichés ([#3962](https://github.com/SocialGouv/egapro/issues/3962), [#4232](https://github.com/SocialGouv/egapro/issues/4232)).
- **Tests et Qualité** :
    - Extension majeure de la couverture de tests de bout en bout (E2E) pour couvrir l'ensemble des parcours utilisateurs ([#4097](https://github.com/SocialGouv/egapro/issues/4097)).
    - Nettoyage et alignement de la nomenclature des tests sur les spécifications ([#4006](https://github.com/SocialGouv/egapro/issues/4006), [#3988](https://github.com/SocialGouv/egapro/issues/3988)).
- **CI/CD et Infrastructure** :
    - Automatisation de la génération des changelogs via IA lors des releases ([#4046](https://github.com/SocialGouv/egapro/issues/4046), [#3965](https://github.com/SocialGouv/egapro/issues/3965)).
    - Amélioration des environnements de test avec le déploiement d'images versionnées ([#2295501](https://github.com/SocialGouv/egapro/commit/2295501)).
    - Sécurisation des communications vers SUIT via l'implémentation du certificat client mTLS ([#4101](https://github.com/SocialGouv/egapro/issues/4101)).
- **Développement** :
    - Amélioration de l'expérience développeur (DX) avec une authentification simplifiée pour les nouveaux environnements de travail (worktrees) ([#4095](https://github.com/SocialGouv/egapro/issues/4095)).

### Autres changements
- **Documentation** : Mise à jour de la documentation technique concernant les règles d'autorité du moteur d'étapes (FSM) et la nomenclature des cas de tests ([#3982](https://github.com/SocialGouv/egapro/issues/3982), [#4006](https://github.com/SocialGouv/egapro/issues/4006)).
