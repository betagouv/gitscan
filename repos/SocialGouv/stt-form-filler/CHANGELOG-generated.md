## Changelog : stt-form-filler (30 derniers jours, au 10/11/2026)

### Résumé
L'outil permet désormais de remplir la partie B du formulaire MDPH grâce à une interface vocale. Cette période a été marquée par une optimisation majeure de la réactivité de la synthèse vocale et une refonte complète de l'infrastructure de déploiement pour garantir une meilleure stabilité et performance sur les serveurs.

### Évolutions fonctionnelles
- **Remplissage vocal** : Mise en place de la fonctionnalité principale permettant de compléter le formulaire MDPH (partie B) par la voix.
- **Améliorations de l'interface (UI)** :
    - Ajout d'un menu latéral pour naviguer entre les questions de l'étape en cours.
    - Intégration des réglages de la voix directement dans l'en-tête.
    - Refonte de l'écran d'introduction (« Avant de commencer ») et amélioration de l'indicateur d'étapes.
- **Ergonomie (UX)** : Possibilité de déclencher la parole via la barre d'espace.
- **Correction de calcul** : Les montants financiers conservent désormais leurs centimes au lieu d'être arrondis à l'euro près.

### Évolutions techniques
- **Optimisation de la performance** : Réduction drastique du temps de synthèse vocale (Piper), passant de 2,7s à 0,3s par phrase, grâce à une gestion optimisée des ressources CPU du conteneur.
- **Refonte de la CI/CD et du déploiement** :
    - Automatisation de la construction des images Docker au sein du cluster OVH/GitHub Actions et poussée vers Harbor.
    - Sécurisation des déploiements via le scellement des secrets (kubeseal) et l'utilisation de jetons dédiés pour les dépôts privés.
    - Mise en place d'un environnement de développement complet sur la "fabrique" (Rancher, cluster OVH).
- **Architecture IA** : Généralisation du fournisseur de LLM pour supporter n'importe quelle API compatible avec le standard OpenAI (Albert est utilisé par défaut).

### Autres changements
- **Documentation** : Mise à jour de la documentation utilisateur incluant le nouveau parcours (fil d'Ariane, questions de suivi, pages légales).
