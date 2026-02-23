## Changelog : eva-serveur (30 derniers jours)

### Résumé
Les dernières mises à jour d'eva-serveur se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'introduction d'une nouvelle interface pour Eva Pro et des corrections de bugs. Des améliorations techniques ont également été apportées, notamment la refactorisation du code, la mise à jour des dépendances et l'amélioration de la gestion des OPCO.

### Évolutions fonctionnelles
- Ajout de l'URL de contact de l'OPCO dans l'évaluation Eva Pro (#bb0eb73).
- Les superadmins peuvent maintenant déplacer le dernier administrateur d'une structure (#993f22a).
- Possibilité de modifier et de consulter l'URL de contact d'un OPCO dans l'interface d'administration (#d516853).
- Ajout d'un nouveau champ `url_contact` sur la table `Opcos` (#0dcb385).
- Les utilisateurs peuvent télécharger le rapport PDF d'une évaluation Eva Pro (#c82b53d).
- Affichage du logo de l'OPCO financeur sur le résultat d'une évaluation (#d272749).
- Ajout d'un composant pour afficher les chiffres clés et le bilan d'une évaluation Eva Pro (#9f84b4a).
- Ajout d'une section "Cinq dernières évaluations" et "Dernière réponse complète" au tableau de bord (#aa53be8, #66cc023).
- Amélioration de l'affichage des coûts sur la page des évaluations Eva Pro (#b2169ad).
- Correction de l'affichage des évaluations de positionnement dans le détail d'un bénéficiaire (#5b73e12, #20fe056).
- Ajout d'une validation du SIRET sur le compte utilisateur (#9db8994).
- Possibilité de recréer ou réimporter un questionnaire avec le nom technique d'un questionnaire effacé (#ed96e4d).

### Évolutions techniques
- Refactorisation de la gestion des OPCO et des campagnes (#68e9f36, #900e414, #a9b5edc, #5239c69).
- Sépare les vues d'évaluation entre Eva et Eva Pro (#96c5aba).
- Ajout d'un composant `BoutonDsfr` pour une gestion améliorée des boutons dans l'interface (#297bdfe).
- Suppression du code devenu inutile (#edda441).
- Suppression du modèle `StructureOpco` et migration des données (#728f9ac, #5a5ca5f).
- Mise à jour des dépendances : Rack, Faraday, aws-sdk-s3, nokogiri (#9319244, #22f96f5, #47749f0, #223e908).
- Suppression de la configuration Mailjet pour le tracking (#9ab6c80).
- Suppression des autorisations de campagne privées lors de la suppression d'un compte (#acc7be8).
- Correction d'une erreur 500 lors de l'affichage d'une campagne privée avec des autorisations orphelines (#5370d1f).
- Correction des redirections après la suppression d'une évaluation (#df8c17d).
- Suppression de la duplication de code dans l'admin (#e101252).
- Suppression de la duplication des champs input et du lien de l'annuaire (#9db8994, #92bd092).
- Suppression de code CSS en commentaire (#b4f8301).
- Amélioration de la gestion des erreurs et des tests (#c2d0275, #95ffe19).

### Autres changements
- Mise à jour de la documentation et des traductions (#f914cbd, #025fb13).
- Amélioration du style et de la mise en page de l'interface utilisateur (#fcfbcdf, #bb7f13c, #a49f735, #6e016ec, #3596a9c, #2fab9a9, #94943a1, #6bda929, #5541eac, #84714cf, #4537c56, #880da47).
- Correction de typos et amélioration de la lisibilité du code (#d9f95af, #812b9ad, #74e30e0, #76f35e1).
- Ajout de tests unitaires (#c82d599).
- Suppression d'un test de feature obsolète (#bce0ad9).
- Ajout d'une variable d'environnement pour activer/désactiver Eva Pro (#c2d0275).
- Correction de bugs mineurs et améliorations de la performance.
