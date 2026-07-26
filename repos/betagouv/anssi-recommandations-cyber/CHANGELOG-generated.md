## Changelog : anssi-recommandations-cyber (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment concernant l'affichage des sources des réponses, la gestion des documents PDF, et l'ajout d'un système d'avis utilisateur. Des corrections et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application. Des renforcements de la sécurité ont été mis en place.

### Évolutions fonctionnelles
- Ajout d'un bouton pour copier les sources de la réponse.
- Amélioration de l'affichage des sources : affichage sur toute la largeur, carrousel pour les pages PDF, et image générique si le document n'est pas un PDF.
- Possibilité de soumettre un avis utilisateur sur la complétude et l'exactitude des réponses.
- Retourne le nom du document ainsi que sa date de mise à jour dans l'interface.
- Affiche le titre du document au lieu du nom du fichier.
- Ajout d'un bouton pour copier les sources de la réponse.
- Ajout de wording spécifique pour les tests internes de l'ANSSI.
- Amélioration de la génération des pages PDF, même en cas d'erreur.
- Ajout d'une documentation sur les interactions entre MQC et Albert.
- Ajout d'icônes DSFR aux boutons du carrousel.
- Passage du bouton de copie en bouton tertiaire.
- Modification des messages d'accueil et de retour.
- Aération des réponses détaillées pour une meilleure lisibilité.

### Évolutions techniques
- Sécurisation du vocabulaire utilisé dans le prompt pour une portée juridique précise.
- Ajout de `zizmor` pour valider la configuration et renforcer la sécurité.
- Désactivation des identifiants `git` des dépôts clonés pour améliorer la sécurité du CI/CD.
- Refactorisation du code pour séparer la réponse de l'API du traitement métier (classe `ParagrapheReponseQuestion`).
- Injection du reclasseur dans le service Albert.
- Suppression de champs obsolètes.
- Harmonisation du nombre de résultats retournés par la recherche.
- Correction de la redirection exécutée par FastAPI lors de l'appel à la ressource `/source`.
- Correction du scroll horizontal des sources.
- Correction de l'activation du bouton "suivant" lorsque les sources sont chargées.
- Amélioration de la gestion des erreurs lors de la génération des pages PDF.
- Renforcement du prompt pour ne plus retenir les sommaires, citations, etc.
- Canonisation des questions reformulées.
- Ajout du paramètre `température` à 0 pour les appels à Albert.
- Suppression du feature flag `reclassement`.
- Suppression d'un console.log dans l'adaptateur PDF du front-end.
- Ajout des raisons des sources non adaptées dans l’événement journalisé.
- Modification de l’API pour prendre en compte le nouveau modèle basé sur les sources adaptées et la pertinence.
- Renommage de fichiers et de constantes pour une meilleure organisation du code.

### Autres changements
- Mise à jour de plusieurs dépendances (vitest, prettier-plugin-svelte, marked, @lab-anssi/ui-kit, dompurify, codeql-action, setup-uv, setup-python).
- Suppression de code inutile et formatage du code pour une meilleure lisibilité.
- Ajout de tests et amélioration de la couverture de test.
- Validation de la longueur des commentaires et des saisies utilisateur.
- Amélioration de la documentation.
