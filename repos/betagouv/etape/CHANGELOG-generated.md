## Changelog : etape (30 derniers jours, au 05/08/2026)

### Résumé
Le projet a connu une progression majeure, passant d'une structure initiale à un site complet et fonctionnel. Les efforts se sont concentrés sur l'intégration de la page d'accueil, le développement du parcours complet du simulateur d'éligibilité et la mise en place d'un système de design robuste pour garantir une expérience utilisateur fluide et accessible.

### Évolutions fonctionnelles
- **Simulateur d'éligibilité** :
    - Intégration du parcours complet des questions et du flux de navigation.
    - Amélioration de l'autocomplétion des communes avec une interface plus accessible et des états de statut clairs.
    - Ajout d'une sécurité de navigation : confirmation de sortie lors de la première question et amélioration du retour en arrière.
    - Optimisation des résultats : les dispositifs non éligibles sont désormais clairement identifiés au lieu d'être simplement filtrés.
- **Personnalisation des liens et résultats** :
    - Régionalisation des liens vers les portails "Avenir Actifs" en fonction de la localisation (travail/résidence) de l'utilisateur [#12](https://github.com/betagouv/etape/pull/12).
    - Affinement des liens CPF pour les agents publics en les distinguant par versant (État, territorial, hospitalier).
    - Suppression des doublons d'URL pour les services CEP.
- **Site vitrine** :
    - Mise en ligne de la page d'accueil avec son contenu éditorial et ses visuels.
    - Intégration d'une section FAQ via un composant accordéon [#13](https://github.com/betagouv/etape/pull/13).
    - Ajout d'une navigation complète incluant un menu, un pied de page et un bouton de retour en haut de page.
    - Mise à jour des éléments de réassurance (ex: remplacement de "Sans engagement" par "Tous profils").

### Évolutions techniques
- **Architecture et infrastructure** :
    - Mise en place d'un monorepo utilisant Turborepo.
    - Déploiement de l'application simulateur en mode SSG (Static Site Generation) pour optimiser les performances.
    - Automatisation des déploiements de prévisualisation via Vercel [#9](https://github.com/betagouv/etape/pull/9).
- **Design System et UI** :
    - Création d'une bibliothèque de composants partagés (basée sur Shadcn UI et Radix UI) incluant les boutons, cartes, accordéons, onglets et sections.
    - Implémentation d'une échelle typographique responsive et de breakpoints conformes aux maquettes.
    - Migration des icônes vers la bibliothèque Lucide.
- **Accessibilité (A11y)** :
    - Renforcement de la navigation au clavier et gestion des anneaux de focus.
    - Implémentation de liens d'évitement (SkipLinks) et de conteneurs accessibles.
    - Refonte de l'autocomplétion des communes pour respecter les standards d'accessibilité (APG).

### Autres changements
- **Qualité de code** : Centralisation de la configuration ESLint et Prettier pour l'ensemble du projet [#2](https://github.com/betagouv/etape/pull/2).
- **Documentation et workflow** : 
    - Mise à jour du README (ajustement de la terminologie "salarié").
    - Ajout d'un modèle de Pull Request pour faciliter les contributions.
    - Configuration du `.gitignore` pour la sécurité des variables d'environnement.
