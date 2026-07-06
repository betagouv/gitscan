## Changelog : tchap-web-v4 (30 derniers jours, au 2026-07-04)

### Résumé
Cette version apporte des améliorations de stabilité et de correction de bugs, notamment concernant la gestion des appels, l'intégration avec l'environnement de construction Scalingo, et la compatibilité avec la nouvelle version d'Element Call (EC). Des ajustements ont également été faits pour améliorer l'expérience utilisateur, notamment concernant les invitations et les pièces jointes.

### Évolutions fonctionnelles
- Correction d'une régression concernant l'intégration de l'appel embarqué (element-call-embedded) avec webpack, et nettoyage des éléments liés à l'ancienne version d'EC. [#1633](https://github.com/tchapgouv/tchap-web-v4/issues/1633)
- Suppression de l'option d'appel hérité en DM si le flag de fonctionnalité `ec_dm` est activé. [#1632](https://github.com/tchapgouv/tchap-web-v4/issues/1632)
- Amélioration du flux d'invitation externe : copie-coller d'invitations corrigée pour les salles externes. [#1609](https://github.com/tchapgouv/tchap-web-v4/issues/1609)
- Mise à jour du bouton de la page de vérification d'email.
- Amélioration de la robustesse du flux d'invitation externe.
- Retour à la valeur par défaut des salles privées si aucune règle d'accès n'est définie et que la salle est chiffrée.
- Acceptation automatique des permissions des widgets EC pour s'aligner avec la nouvelle version d'EC.
- Mise à jour du comportement de téléchargement sur le bureau : seul le nom du fichier est envoyé.
- Mise à jour du message d'erreur.

### Évolutions techniques
- Mise à jour de la version d'Element vers 1.12.17. [#1596](https://github.com/tchapgouv/tchap-web-v4/issues/1596)
- Correction d'un problème de construction avec Scalingo. [#1631](https://github.com/tchapgouv/tchap-web-v4/issues/1631)
- Mise à jour de la configuration de test et correction d'un problème avec l'invitation dans le dialogue d'invitation externe.
- Mise à jour des versions de Node.js et pnpm dans les workflows.
- Suppression d'un plugin Tauri inutilisé.
- Mise à jour des dépendances vers la version 4.20.0.
- Suppression du test "roots" et mise à jour des tests de fusion.
- Suppression du module hérité de traduction.
- Mise à jour de l'importation du chiffrement et utilisation de l'onglet des paramètres privés.
- Mise à jour de la configuration du workflow.
- Ajout de la possibilité de mise à jour automatique sur le bureau.
- Corrections de sécurité mineures sur le bureau.
- Réactivation de l'option de la liste rouge.

### Autres changements
- Mise à jour de la documentation README après la monoreposisation.
- Correction de quelques erreurs de lint.
- Mise à jour du script eslint.
- Ajout de la gestion des fichiers contenus dans les vues.
- Ajout d'un gestionnaire de bouton de barre d'action.
- Correction de la traduction TCHAP.
- Ajout d'une traduction manquante.
